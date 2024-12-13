<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Formulário Digital</title>
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
	    border: 10px;
            border-radius: 6px;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
        }
        h1 {
            font-family: Arial, sans-serif;;
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
            <div class="section">
                
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
            </div>

            <!-- Adicionar outros campos aqui -->

            <button type="submit" class="submit-button">Enviar</button>
        </form>
    </div>

    <script src="https://cdnjs.cloudflare.com/ajax/libs/jspdf/2.4.0/jspdf.umd.min.js"></script>
    <script>
        document.getElementById('cadastro-form').addEventListener('submit', function(e) {
            e.preventDefault();

            const nome = document.getElementById('nome').value;
            const email = document.getElementById('email').value;
            const telefone = document.getElementById('telefone').value;
            const cpf = document.getElementById('cpf').value;
            const dataNascimento = document.getElementById('data-nascimento').value;
            const rg = document.getElementById('rg').value;
            const dataEmissao = document.getElementById('data-emissao').value;
            const naturalidade = document.getElementById('naturalidade').value;
            const nacionalidade = document.getElementById('nacionalidade').value;
            const estadoCivil = document.getElementById('estado-civil').value;
            const conjuge = document.getElementById('conjuge').value;
            const rendimentoConjuge = document.getElementById('rendimento-conjuge').value;
            const rendimentoTitular = document.getElementById('rendimento-titular').value;
            const atividade = document.getElementById('atividade').value;
            const nomeMae = document.getElementById('nome-mae').value;
            const nomePai = document.getElementById('nome-pai').value;

            // Gerar PDF com as informações preenchidas
            const { jsPDF } = window.jspdf;
            const doc = new jsPDF();

            doc.setFont('Helvetica', 'normal');
            doc.setFontSize(12);

            doc.text('Formulário de Cadastro', 105, 20, { align: 'center' });

            doc.text(`Nome do Cliente: ${nome}`, 20, 40);
            doc.text(`E-mail do Cliente: ${email}`, 20, 50);
            doc.text(`Telefone(s) do Cliente: ${telefone}`, 20, 60);
            doc.text(`CPF: ${cpf}`, 20, 70);
            doc.text(`Data de Nascimento: ${dataNascimento}`, 20, 80);
            doc.text(`RG e Órgão Emissor: ${rg}`, 20, 90);
            doc.text(`Data de Emissão: ${dataEmissao}`, 20, 100);
            doc.text(`Naturalidade: ${naturalidade}`, 20, 110);
            doc.text(`Nacionalidade: ${nacionalidade}`, 20, 120);
            doc.text(`Estado Civil: ${estadoCivil}`, 20, 130);
            doc.text(`Cônjuge: ${conjuge}`, 20, 140);
            doc.text(`Rendimento do Cônjuge: ${rendimentoConjuge}`, 20, 150);
            doc.text(`Rendimento do Titular: ${rendimentoTitular}`, 20, 160);
            doc.text(`Atividade Desenvolvida do Titular: ${atividade}`, 20, 170);
            doc.text(`Nome da Mãe: ${nomeMae}`, 20, 180);
            doc.text(`Nome do Pai: ${nomePai}`, 20, 190);

    // Converte o PDF para um blob
    const pdfBlob = doc.output('blob');

    // Enviar para WhatsApp
    const whatsappNumber = '559870002002';
    const pdfFile = new File([pdfBlob], `Formulario_${nome.replace(/\s+/g, '_')}.pdf`, { type: 'application/pdf' });

    // Criar um link para enviar no WhatsApp
    const formData = new FormData();
    formData.append('file', pdfFile);
    
    const pdfURL = URL.createObjectURL(pdfBlob); // Cria o link temporário para o PDF

    // Abre o WhatsApp no navegador do celular
    const whatsappLink = `https://wa.me/${whatsappNumber}?text=Segue%20o%20formulário%20preenchido:%20${encodeURIComponent(pdfURL)}`;
    window.open(whatsappLink, '_blank');
});

    </script>
</body>
</html>
