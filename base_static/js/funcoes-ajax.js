function utilizouHoraExtra(hora_extra_id, funcionario_id) {
    token = document.getElementsByName('csrfmiddlewaretoken')[0].value

    $.ajax({
        type: 'POST',
        url: '/horas-extras/utilizou-hora-extra/' + hora_extra_id,
        data: {
            csrfmiddlewaretoken: token,
            funcionario_id: funcionario_id
        },
        success: function(result) {
            $('#mensagem').text(result.message)
            $('#horas_atualizadas').text(result.horas)
        }
    })
}

function naoUtilizouHoraExtra(hora_extra_id, funcionario_id) {
    token = document.getElementsByName('csrfmiddlewaretoken')[0].value

    $.ajax({
        type: 'POST',
        url: '/horas-extras/nao-utilizou-hora-extra/' + hora_extra_id,
        data: {
            csrfmiddlewaretoken: token,
            funcionario_id: funcionario_id
        },
        success: function(result) {
            $('#mensagem').text(result.message)
            $('#horas_atualizadas').text(result.horas)
        }
    })
}