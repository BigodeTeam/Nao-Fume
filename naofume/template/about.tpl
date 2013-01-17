{% extends 'base.tpl' %}
{% block body_attr %}data-page="landing"{% endblock %}
{% block title %}Sobre - Não Fu.me - Um jeito simples de traçar sua meta para largar de vez o cigarro.{% endblock %}
{% block body %}
    {% load staticfiles %}
    {% include 'nav_header.tpl' %}
    <div class="g960 landing" xmlns="http://www.w3.org/1999/html" xmlns="http://www.w3.org/1999/html">
        <header>
            <div class="g555">
                <h1 class="logo"><a href="/">Não Fu.me</a></h1>
                <h2>Menos fumaça, <br> Mais saúde.</h2>
                <p>Um jeito simples de traçar sua meta para largar de vez o cigarro.</p>
            </div>
        </header>

        <div class="institucional">
            <p>Tratar a dependência do cigarro é uma ardua tarefa, pois além da dependência física há uma dependência psicológica muito grande. O NãoFu.me foi criado para ajudar você, fumante que precisa de incentivos e metas para largar o vício.</p>
            <p>O segredo está em assumir que o tabagismo é uma doença e agüentar o tempo de tratamento, que pode levar meses, sabendo que vai vale a pena todo esforço.</p>
            <p>É fundamental marcar uma data para parar de fumar, mesmo que isso não seja uma garantia. É muito provavél que você ainda não está preparado para tomar a iniciativa de enfrentar a abstinência.</p>
            <p>É comum os fumantes que fixam uma data gostarem de divulgar suas metas, esperando ajuda e incentivos. Convidar seus amigos e postar seu progresso no facebook pode ser muito util! Mas há quem prefere manter o silencio e evitar que algum fracasso possa abalar sua autoestima, caso prefire o silencio cadastre-se como perfil privado.</p>
            
            <h3 class="h3">Com o NãoFu.me você pode</h3>
            <ul>
                <li>- Criar sua meta</li>
                <li>- Ver quanto está economizando</li>
                <li>- Recer incentivos dos amigos e do NãoFu.me</li>
                <li>- Ver e incentivar o progresso dos seus amigos</li>
            </ul>
            
            <h3 class="h3">NãoFu.me - criado e desenvolvido durante o <a target="_blank" href="http://startupdev.com.br/rumble/pt/">StartupDev Rumble</a> por:</h3>
            <div class="gato"><a href="https://github.com/CiceroComp">
                <img width="140" height="140" src="https://secure.gravatar.com/avatar/80a609d8054c9aa272e22ddc019b80f1?s=140&d=https://a248.e.akamai.net/assets.github.com%2Fimages%2Fgravatars%2Fgravatar-user-420.png" alt="">
                Cicero Verneck
            </a></div>
            <div class="gato"><a href="https://github.com/diogocorrea">
                <img width="140" height="140" src="https://secure.gravatar.com/avatar/904f4796068daaec2582e3d1138dafcf?s=140&d=https://a248.e.akamai.net/assets.github.com%2Fimages%2Fgravatars%2Fgravatar-user-420.png" alt="">
                Diogo Corrêa
            </a></div>
            <div class="gato"><a href="https://github.com/pantuza">
                <img width="140" height="140" src="https://secure.gravatar.com/avatar/b1412c9ed55333c1df561f64dfad69d3?s=140&d=https://a248.e.akamai.net/assets.github.com%2Fimages%2Fgravatars%2Fgravatar-user-420.png" alt="">
                Gustavo Pantuza
            </a></div>
            <div class="gato"><a href="https://github.com/vitalbh">
                <img width="140" height="140" src="https://secure.gravatar.com/avatar/ccd23e7788b7bab2647e02b338fdbcb7?s=140&d=https://a248.e.akamai.net/assets.github.com%2Fimages%2Fgravatars%2Fgravatar-user-420.png" alt="">
                Victor Hugo
            </a></div>
        </div>

    </div>
{% endblock %}