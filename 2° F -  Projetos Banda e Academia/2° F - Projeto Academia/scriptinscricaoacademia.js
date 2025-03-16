document.getElementById("formInscricao").addEventListener("submit", function (e) {
    e.preventDefault();
    const nome = document.getElementById("nome").value.trim();
    const cep = document.getElementById("cep").value.trim();
    const telefoneResidencial = document.getElementById("telefoneResidencial").value.trim();
    const telefoneCelular = document.getElementById("telefoneCelular").value.trim();
    const cpf = document.getElementById("cpf").value.trim();

    let mensagem = "";

    if (nome === "") {
        mensagem += "⚠️ Nome é obrigatório.<br>";
    }
    if (!cep.match(/^\d{5}-\d{3}$/)) {
        mensagem += "⚠️ CEP deve estar no formato XXXXX-XXX.<br>";
    }
    if (!telefoneResidencial.match(/^\(\d{2}\) \d{4}-\d{4}$/)) {
        mensagem += "⚠️ Telefone Residencial deve estar no formato (XX) XXXX-XXXX.<br>";
    }
    if (!telefoneCelular.match(/^\(\d{2}\) \d{5}-\d{4}$/)) {
        mensagem += "⚠️ Telefone Celular deve estar no formato (XX) XXXXX-XXXX.<br>";
    }
    if (!cpf.match(/^\d{3}\.\d{3}\.\d{3}-\d{2}$/)) {
        mensagem += "⚠️ CPF deve estar no formato XXX.XXX.XXX-XX.<br>";
    }

    const mensagemElement = document.getElementById("mensagem");
    if (mensagem !== "") {
        mensagemElement.innerHTML = mensagem;
        mensagemElement.style.color = "#dc3545";
    } else {
        mensagemElement.innerHTML = "✅ Formulário enviado com sucesso!";
        mensagemElement.style.color = "#28a745";
    }
});
