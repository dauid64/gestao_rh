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

function process_response(funcionarios) {
    func_select = document.getElementById('funcionarios')
    func_select.innerHTML = ""

    funcionarios.forEach(funcionario => {
        var option = document.createElement('option')
        option.text = funcionario.fields.nome
        func_select.add(option)
    })
}

function filtraFuncionarios() {
    depart_id = document.getElementById('departamentos').value

    $.ajax({
        type: 'GET',
        url: '/filtra-funcionarios/',
        data: {
            depart_id: depart_id
        },
        success: function(result) {
            process_response(result)
            $('#mensagem').text('Funcionários carregados!')
        }
    })
}
