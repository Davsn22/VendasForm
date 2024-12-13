<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>VendasForm</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background-color: #f9f9f9;
            margin: 0;
            padding: 20px;
        }
        .form-container {
            max-width: 700px;
            margin: auto;
            background: white;
            padding: 10px;
            border-radius: 6px;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
        }
        h1 {
            font-family: Arial, sans-serif;
            text-align: center;
        }
        label {
            font-family: Arial, sans-serif;
            font-size: 10px;
            font-weight: bold;
        }
        input, select {
            width: calc(100% - 20px);
            padding: 10px;
            margin: 2px 2px 4px 4px;
            border: 1px solid #ccc;
            border-radius: 6px;
            font-size: 10px;
            box-sizing: border-box;
        }
        .row {
            display: flex;
            gap: 20px;
        }
        .column {
            flex: 1;
        }
        .submit-button {
            background-color: #4CAF50;
            color: white;
            padding: 10px;
            border: none;
            border-radius: 4px;
            cursor: pointer;
            font-size: 16px;
        }
        .submit-button:hover {
            background-color: #45a049;
        }
    </style>
    <link href="https://fonts.googleapis.com/css2?family=Dancing+Script:wght@400;600&display=swap" rel="stylesheet">
</head>
<body>
    <div class="form-container">
        <h1>DADOS DO CONSORCIADO</h1>
        <form id="cadastro-form">
            <label for="nome">Nome do Cliente:</label>
            <input type="text" id="nome" name="nome" required>

            <label for="email">E-mail do Cliente:</label>
            <input type="email" id="email" name="email" required>

            <label for="telefone">Telefone(s) do Cliente:</label>
            <input type="text" id="telefone" name="telefone" required>

            <div class="row">
                <div class="column">
                    <label for="cpf">CPF:</label>
                    <input type="text" id="cpf" name="cpf" required>
                </div>
                <div class="column">
                    <label for="data-nascimento">Data de Nascimento:</label>
                    <input type="date" id="data-nascimento" name="data-nascimento" required>
                </div>
            </div>

            <div class="row">
                <div class="column">
                    <label for="rg">RG e Órgão Emissor:</label>
                    <input type="text" id="rg" name="rg" required>
                </div>
                <div class="column">
                    <label for="data-emissao">Data de Emissão:</label>
                    <input type="date" id="data-emissao" name="data-emissao" required>
                </div>
            </div>

            <div class="row">
                <div class="column">
                    <label for="naturalidade">Naturalidade:</label>
                    <input type="text" id="naturalidade" name="naturalidade" required>
                </div>
                <div class="column">
                    <label for="nacionalidade">Nacionalidade:</label>
                    <input type="text" id="nacionalidade" name="nacionalidade" required>
                </div>
            </div>

            <label for="estado-civil">Estado Civil:</label>
            <input type="text" id="estado-civil" name="estado-civil" required>

            <label for="conjuge">Nome, CPF e Data de Nascimento do Cônjuge:</label>
            <input type="text" id="conjuge" name="conjuge">

            <div class="row">
                <div class="column">
                    <label for="rendimento-conjuge">Rendimento do cônjuge:</label>
                    <input type="number" id="rendimento-conjuge" name="rendimento-conjuge">
                </div>
                <div class="column">
                    <label for="rendimento-titular">Rendimento do titular:</label>
                    <input type="number" id="rendimento-titular" name="rendimento-titular" required>
                </div>
            </div>

            <label for="atividade">Atividade Desenvolvida do Titular:</label>
            <input type="text" id="atividade" name="atividade" required>

            <label for="nome-mae">Nome da Mãe:</label>
            <input type="text" id="nome-mae" name="nome-mae" required>

            <label for="nome-pai">Nome do Pai:</label>
            <input type="text" id="nome-pai" name="nome-pai">

            <button type="submit" class="submit-button">Enviar</button>
        </form>
    </div>

    <script src="https://cdnjs.cloudflare.com/ajax/libs/jspdf/2.4.0/jspdf.umd.min.js"></script>
    <script>
        document.getElementById('cadastro-form').addEventListener('submit', function(e) {
            e.preventDefault();

            const { jsPDF } = window.jspdf;
            const doc = new jsPDF();

            doc.setFont('Times', 'italic');
            doc.setFontSize(14);
            doc.text('Formulário de Pessoa Física', 105, 10, { align: 'center' });

	const fields = [
    { label: '', value: document.getElementById('nome').value, x: 10, y: 20 },
    { label: '', value: document.getElementById('email').value, x: 10, y: 30 },
    { label: '', value: document.getElementById('telefone').value, x: 10, y: 40 },
    { label: '', value: document.getElementById('cpf').value, x: 10, y: 50 },
    { label: 'Data de Nascimento', value: document.getElementById('data-nascimento').value, x: 100, y: 50 },
    { label: 'RG e Órgão Emissor', value: document.getElementById('rg').value, x: 10, y: 60 },
    { label: 'Data de Emissão', value: document.getElementById('data-emissao').value, x: 100, y: 60 },
    { label: 'Naturalidade', value: document.getElementById('naturalidade').value, x: 10, y: 70 },
    { label: 'Nacionalidade', value: document.getElementById('nacionalidade').value, x: 100, y: 70 },
    { label: 'Estado Civil', value: document.getElementById('estado-civil').value, x: 10, y: 80 },
    { label: 'Nome, CPF e DN do Cônjuge', value: document.getElementById('conjuge').value, x: 10, y: 90},
    { label: 'Rendimento do cônjuge', value: document.getElementById('rendimento-conjuge').value, x: 10, y: 100 },
    { label: 'Rendimento do titular', value: document.getElementById('rendimento-titular').value, x: 10, y: 110 },
    { label: 'Atividade Desenvolvida do Titular', value: document.getElementById('atividade').value, x: 10, y: 120 },
    { label: 'Mãe', value: document.getElementById('nome-mae').value, x: 10, y: 130 },
    { label: 'Pai', value: document.getElementById('nome-pai').value, x: 10, y: 140 }
];

fields.forEach(field => {
    doc.text(`${field.label}: ${field.value}`, field.x, field.y);
});


            const pdfBlob = doc.output('blob');
            const pdfURL = URL.createObjectURL(pdfBlob);
            const whatsappNumber = '559870002002';
            const message = `Segue o formulário preenchido em PDF.`;
            const whatsappLink = `https://wa.me/${whatsappNumber}?text=${encodeURIComponent(message)}`;

            const a = document.createElement('a');
            a.href = pdfURL;
            a.download = `Formulario_${document.getElementById('nome').value}.pdf`;
            a.click();

            window.open(whatsappLink, '_blank');
        });
    </script>
</body>
</html>
