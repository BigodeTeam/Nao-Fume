<h2 class="h2">Compartilhe sua evolução</h2>
<form action="#" class="postar-mensagem" id="js-form-post">
    <textarea id="js-post" class="input" placeholder="Compartilhe sua evolução"></textarea>
    <label class="facebook"><input id="js-post-fb" name="post_fb" type="checkbox" {% if USER.privacy == '2'%}checked="checked"{% endif %}> postar no facebbok</label>
    <input type="submit" class="bt" value="Enviar">
</form>