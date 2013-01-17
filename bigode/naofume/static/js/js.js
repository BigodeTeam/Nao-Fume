var Feed = (function() {
    var
        _init, _bindEvents, _keyUsege, _postComment, _deletePost, _showMore,
        _object = {
            user_id: 0
        }
    ;

    _postComment = function() {
        $.ajax({
            url:'/post',
            data: {post: $('#js-post').val(),post_fb:$("#js-post-fb:checked").length},
            type: 'POST'
        }).done(function(e) {
            if(e.status){

                var msg = $('<div/>').text(e.message).html();
                $('#js-post').val('');
                var html = ''
                    +'<div class="post diminuiu" data-id="'+ e.id +'">'
                    +    '<a href="'+ e.username +'/">'
                    +       '<img src="'+ e.picture +'" alt="" width="50" height="50">'
                    +    '</a>'
                    +    '<p class="post-cnt">'
                    +        '<strong>' + e.username + '</strong> '+msg
                    +        '<a href="#" title="excluir mensagem" class="post-delete">-</a>'
                    +    '</p>'
                    + '</div>';

                $('#js-post').parent().after(html);
            }
        });
        return false;
    };

    _deletePost = function(e){
        var $el = $(this).parents('.post')
            id = $el.data('id');
        $.ajax({
            url:'/post?id='+id,
            type: 'DELETE'
        }).done(function(e) {
            if(e.status){
                $el.fadeOut();
            }
        });
        return false;
    };

    _keyUsege = function(e) {
        if(e.keyCode == 13 && e.shiftKey == false){
            _postComment();
            return false;
        }
    };

    _bindEvents = function() {
        $('#js-post').on('keydown', _keyUsege);
        $('#js-form-post').on('submit', _postComment);
        $('body').on('click' ,'.post .post-delete', _deletePost);
        $('body').on('click', '#js-show-more', _showMore);
    };

    _showMore = function(){
        var data = {
            id: $('.post:last').data('id'),
            page:$('body').data('page'),
            username:$('body').data('username')
        };
        $.ajax({
            url:'/post',
            data: data,
            type: 'GET'
        }).done(function(json) {
            var _i,_len, e;
            for(_i = 0, _len = json.data.length; _i < _len; _i++){
                e = json.data[_i];
                var msg = $('<div/>').text(e.message).html();
                $('#js-post').val('');
                var html = ''
                    +'<div class="post '+(e.type==2?"system":"user")+'" data-id="'+ e.id +'">'
                    +    '<a href="'+ e.username +'/">'
                    +       '<img src="'+ e.picture +'" alt="" width="50" height="50">'
                    +    '</a>'
                    +    '<p class="post-cnt">'
                    +        '<strong>' + e.username + '</strong> '+msg
                    +        (e.is_owner?'<a href="#" title="excluir mensagem" class="post-delete">-</a>':'')
                    +    '</p>'
                    + '</div>';

                $('.post:last').after(html);
            }
            if(json.total <= 10){
                $('#js-show-more').remove();
            }
        });
        return false;
    };

    _init = function() {
        _object.user_id = $('.main-nav').data('user-id');
        _bindEvents();
    };

    

    return {
        init: function() {
            _init();
        }
    }
}());

var Chart = (function() {
    var _init;



    _init = function(){
        $.ajax({
            url: '/historico/',
            type: 'get',
            data: {username:$('body').data('username')},
            dataType:'json'
        }).done(function(json){
            var _i,_len, e;
            var dados = [['Data', 'Quantidade']];
            for(_i=0,_len=json.length;_i<_len;_i++){
                e = json[_i].fields;
                e.date = e.date.split('-');
                e.date = [e.date[2],'/', e.date[1],'/', e.date[0]].join('');
                dados.push([e.date, e.amount]);
            }



            var data = google.visualization.arrayToDataTable(dados);

            var options = {
                title: '',
                colors: ['#007C72'],
                legend:{position:'none'},
                pointSize:5
            };

            var chart = new google.visualization.LineChart(document.getElementById('js-chart'));
            chart.draw(data, options);
        });
    };

    return {
        init: function(){
            _init();
        }
    }
}());

function sendRequestViaMultiFriendSelector() {
    FB.ui({method: 'apprequests',

        message: 'Conheça o não fu.me! Um jeito simples de traçar sua meta para largar de vez o cigarro. '

    }, function(){});
}

var Slide = (function(){
    var _init, _run, _count = 1, _time=3000,
        _imgs = [
            '/static/img/slide1.jpg?v=1',
            '/static/img/slide2.jpg?v=1',
            '/static/img/slide3.jpg?v=1',
            '/static/img/slide4.jpg?v=1'
        ];

    _run = function(){
        var img = _imgs[_count % _imgs.length];
        $('<img src="'+img+'" width="455" height="300" alt=""/>').load(function(){
            $('#js-slider').prepend(
                this
            );
            $('#js-slider img:last').fadeOut(1000,function(){
                $(this).remove();
                _count++;
                setTimeout(_run, _time);
            });
        });

    };

    _init = function(){
        setTimeout(_run,_time);
    };

    return {
        init: function(){
            _init();
        }
    }
}());

var userStats = (function(){

    var STATS_URL = "/estatistica/",
    drawVisualization = function(data, options) {

        var dataTable = google.visualization.arrayToDataTable(data),

        chart = new google.visualization.ComboChart(document.getElementById('stats-chart'));
        chart.draw(dataTable, options);
    },

    simpleStatsCallback = function(data){
        var analisys = data.pop(data.length-1).analisys, 
            headers = ['Mês', 'cigarros não fumados', 'economia do período', 'economia diária'],
            options = {
                axisFontSize: 0,
                hAxis : {textColor: '#ffffff'},
                seriesType: "bars",
                series: {2: {type: "line"}},
                legend: {position: 'none'},
                colors: ['#54BDB4','#007C72','#033834']
            },
            dataChart = [],
            i,
            cigarLegend = $(".legenda.cigarro strong"),
            moneyLegend = $(".legenda.dinheiro strong"),
            avgLegend = $(".legenda.media strong");  

        dataChart.push(headers);
            
        //for(i=data.length-1;i>=0;i--){
        for(i=0;i<=data.length-1;i++){
            dataChart.push([
                data[i].date, 
                data[i].amount, 
                parseFloat(data[i].saved), 
                parseFloat(data[i].avg)
            ]);
        }

        drawVisualization(dataChart, options);
        
        if(analisys.hasOwnProperty('not_smoked')){
            cigarLegend.text(analisys.not_smoked.value);
            moneyLegend.text(analisys.saved.value);
            avgLegend.text(analisys.global_avg.value);
        } else {
            $(".legenda").remove();
        } 
    },
    
    errorFunction = function(msg){
        console.error(msg);
    },
    
    successFunction = function(json, callback){
        if(json.length > 0 && typeof callback === "function"){
            callback(json);
        } else {
            errorFunction("invalid json object");
        }
    },

    getUserStats = function(method, callback){
        var requestData = {
            url: [STATS_URL, method, "/", $("body").data("username")].join(''),
            dataType: "json",
            type: "GET",
            success: function(json){successFunction(json, callback);},
            error: errorFunction
        };

        $.ajax(requestData);
    },

    start = function(method){
        if(typeof method === "string"&&  method === "simples"){
            getUserStats(method, simpleStatsCallback);
        }
    };

    return {start: function(method){start(method);}}
})();

$(function(){

    switch ($('body').data('page')){
        case 'home':
            Feed.init();
            HistoryBox.init();
            break;
        case 'profile':
            Feed.init();
            HistoryBox.init();
            break;
        case 'register':
            Register.init();
            break;
        case 'landing':
            Slide.init();
    }
    $('.perfil-amigos .bt,.lista-amigos .bt').click(sendRequestViaMultiFriendSelector);
});




var HistoryBox = (function() {
    var
        _init,_set_events,_postHistory,_validate_amount_number,
        _object = {
            box:''
        }
        ;

    _init = function(){
        _object.box = $('#js-form-post-history');
        _set_events();

    };

    _set_events = function(){
        _object.box.submit(function(){

            if(_validate_amount_number(_object.box.find('input:first')) ){
                _postHistory();
                return false;
            }else
                return false;

        });

        _object.box.find('a.bt-atualizar').click(function(){
            _object.box.trigger('submit');
            return false;
        });



    };
    _postHistory = function() {
        $.ajax({
            url:'/historico/',
            data: {amount: _object.box.find('input:first').val(),cigarette: _object.box.find('select').val(),post_fb:_object.box.find('input:last:checked').length},
            type: 'POST'
        }).done(function(e) {
                if(e.status){

                    var msg = $('<div/>').text(e.message).html();
                    $('#js-post').val('');
                    var html = ''
                        +'<div class="post '+(e.type==2?"system":"user")+'" data-id="'+ e.id +'">'
                        +    '<a href="'+ e.username +'/">'
                        +       '<img src="'+ e.picture +'" alt="" width="50" height="50">'
                        +    '</a>'
                        +    '<p class="post-cnt">'
                        +        '<strong>' + e.username + '</strong> '+msg
                        +        '<a href="#" title="excluir mensagem" class="post-delete">-</a>'
                        +    '</p>'
                        + '</div>';

                    $('#js-post').parent().after(html);
                }
            });
        return false;
    };

    _validate_amount_number = function(amount_number){
        var number = parseInt(amount_number.val(), 10);

        if(number < 0){
            amount_number.val(0);
            return false;
        }else{
            return true;
        }
    };

    return {
        init: function(){
            _init();
        }
    }
}());

var Register = (function() {
    var
        _init,
        _object = {
            user_id: 0
        }
        ;

    _init = function(){
        _object.user_id = $('.header-cadastro').data('user-id');

        _set_events();
    };

    _set_events = function(){

        $("#js-goal-number").blur(_validate_goal_number);
        $("#js-amount-number").blur(_validate_goal_number);

        $("form").submit(function(){

            if(_validate_goal_number("#js-goal-number") && _validate_goal_number("#js-amount-number") )
                return true;
            else
                return false;

        });


    };

    _validate_goal_number = function(e){
        if(e.target)
            var goal_number = $(e.target);
        else
            var goal_number = $(e);

        if($.trim(goal_number.val()).length == 0){
            goal_number.addClass('error').siblings('.erro').show();
            return false;

        }else{
            goal_number.removeClass('error').siblings('.erro').hide();
            return true;
        }
    };

    return {
        init: function(){
            _init();
        }
    }
}());

(function(d, s, id) {
var js, fjs = d.getElementsByTagName(s)[0];
if (d.getElementById(id)) return;
js = d.createElement(s); js.id = id;
js.src = "//connect.facebook.net/pt_BR/all.js#xfbml=1&appId=487995457879029";
fjs.parentNode.insertBefore(js, fjs);
}(document, 'script', 'facebook-jssdk'));



var _gaq = _gaq || [];
_gaq.push(['_setAccount', 'UA-34501459-1']);
_gaq.push(['_trackPageview']);

(function() {
    var ga = document.createElement('script'); ga.type = 'text/javascript'; ga.async = true;
    ga.src = ('https:' == document.location.protocol ? 'https://ssl' : 'http://www') + '.google-analytics.com/ga.js';
    var s = document.getElementsByTagName('script')[0]; s.parentNode.insertBefore(ga, s);
    })();

