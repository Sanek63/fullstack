var id = 0;

document.addEventListener('readystatechange', event => {

    if (event.target.readyState === "interactive") {      //same as:  document.addEventListener("DOMContentLoaded"...   // same as  jQuery.ready

    }

    if (event.target.readyState === "complete") {
        getSortedDataByDamage('Name')
    }

});

function add(){
    const name_heroe = document.getElementById('name_heroe').value;// read about const let and var
    const count_health = document.getElementById('count_health').value;
    const damage = document.getElementById('damage').value;
    const mana = document.getElementById('mana').value;

    var atribute_element = document.getElementById('attribute');
    var atribute = atribute_element.value;

    var is_correct_input = true;

    /* Поле имени */
    if(del_spaces(name_heroe) === '') { // find difference between == and ===
        show_clear_field('Название героя')
        is_correct_input = false;
    }

    /* Поле здоровья */
    if(del_spaces(count_health) === '') {
        show_clear_field('Количество здоровья')
        is_correct_input = false;
    }
    if(!parseInt(count_health)){
        show_incorrect_field('Количество здоровья');
        is_correct_input = false;   
    }

    /* Поле урона */
    if(del_spaces(damage) === '') {
        show_clear_field('Урон')
        is_correct_input = false;   
    }
    if(!parseInt(damage)){
        show_incorrect_field('Урон');
        is_correct_input = false;   
    }

    /* Поле маны */
    if(del_spaces(mana) === '') {
        show_clear_field('Мана')
        is_correct_input = false;
    }
    if(!parseInt(mana)){
        show_incorrect_field('Мана');
        is_correct_input = false;   
    }
    
    if(is_correct_input){
        post_hero(name_heroe, count_health, damage, mana, atribute);
    }
}

function sendHttpRequest(method, url, data) {
    return new Promise((resolve, reject) => {
        const xhr = new XMLHttpRequest();

        xhr.open(method, url);

        xhr.responseType = 'json';

        xhr.onload = () => {
            if (xhr.status >= 400) {
                reject(xhr);
            } else {
                resolve(xhr);
            }
        };
        xhr.onerror = () => {
            reject('Something went wrong')
        }
            xhr.send(JSON.stringify(data));



    }).catch(err => {
        if(err.errorCode === undefined){
            alert('Ошибка с соединением сервера')
        }
    });
}


function getSortedDataByDamage(attribute){
    sendHttpRequest('POST', 'http://127.0.0.1:5000/get_sorted',
        {attribute: attribute}).then(
            responseData => {
                if(responseData.status === 200){
                    document.getElementsByClassName('block-results-content')[0].innerHTML = "";
                    let data = responseData.response;
                    for (let index = 0; index <= data['count']; index++){
                        id = data['items'][index]['id']
                        name = data['items'][index]['name']
                        health = data['items'][index]['health']
                        damage = data['items'][index]['damage']
                        mana = data['items'][index]['mana']
                        attribute = data['items'][index]['attribute']

                        add_heroe(id, name, health, damage, mana, attribute)
            }
        }

    }).catch(err => {
        if(err.errorCode !== undefined){
            alert('Ошибка добавления героя')
        }
    });
}

function post_hero(name_heroe, count_health, damage, mana, attribute){
    sendHttpRequest('POST', 'http://127.0.0.1:5000/add', {
        name: name_heroe,
        health: count_health,
        damage: damage,
        mana: mana,
        attribute: attribute
    }).then(responseData => {
        if(responseData.status === 200){
            let id = responseData.response['id'];
            add_heroe(id, name_heroe, count_health, damage, mana, attribute);
        }
    }).catch(err => {

    });
}

function add_heroe(id, name_heroe, count_health, damage, mana, attribute){
    document.getElementsByClassName('block-results-content')[0].innerHTML +=
    `<div id = "hero_${id}" class="block-heroe">
        <div class="block-heroe-header">
            <div class="name-heroe">
               ${name_heroe}
            </div>
            <button class="button-delete-heroe" onclick="delete_hero('hero_${id}')">Удалить</button>
        </div>
        <div class="hero-haracteristics">
            <div>ID : <b>${id}</b></div>
            <div>Атрибут : <b>${attribute}</b></div>
            <div>Количество здоровья <b>${count_health} HP</b></div>
            <div>Урон : <b>${damage}</b></div>
            <div>Мана : <b>${mana}</b></div>
        </div>
    </div>`;
}

function delete_hero(id){
    sendHttpRequest('POST', 'http://127.0.0.1:5000/remove', {
        id: id
    }).then(responseData => {
        if(responseData.status === 200){
            delete_hero_site(id)
        }
    }).catch(err => {
        alert(err);
    });
}

function delete_hero_site(id){
        var element = document.getElementById(id);
        element.parentNode.removeChild(element);
}

function show_clear_field(field){
    alert(`Поле '${field}' не содержит значения! Проверьте данные`)
}

function show_incorrect_field(field){
    alert(`Поле '${field}' должно быть целым числом!`)
}

function del_spaces(str){
	str = str.replace(/\s/g, '');
	return str;
}
