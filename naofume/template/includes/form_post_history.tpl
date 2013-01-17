<form id="js-form-post-history" action="#" class="perfil-consumo">
    <h3 class="h3">Consumo diário</h3>
    <input type="number" min="0" value="{{ USER.history.amount }}"
           class="input input-inline" />
    <select  class="input input-inline">
        {% for cig in CIGARETTES %}
            <option value="{{ cig.pk }}"
                    {% if USER.history.cigarette.pk == cig.pk %}
                    selected="selected"
                    {% endif %}>
                {{ cig.name }}
            </option>
        {% endfor %}
    </select>
    <span>cigarros</span>
    <label class="facebook"><input type="checkbox" {% if USER.privacy == '2'%}checked="checked"{% endif %}> postar no facebbok</label>
    <a href="#" class="bt bt-atualizar">Atualizar</a>
</form>