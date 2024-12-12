<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Formulário de Cadastro</title>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/jspdf/2.4.0/jspdf.umd.min.js"></script>
</head>
<body>
    <h1>Formulário de Cadastro</h1>
    <form id="cadastro-form">
        <label for="nome">Nome:</label>
        <input type="text" id="nome" name="nome" required><br>

        <label for="email">E-mail:</label>
        <input type="email" id="email" name="email" required><br>

        <label for="telefone">Telefone:</label>
        <input type="text" id="telefone" name="telefone" required><br>

        <label for="cpf">CPF:</label>
        <input type="text" id="cpf" name="cpf" required><br>

        <label for="data-nascimento">Data de Nascimento:</label>
        <input type="date" id="data-nascimento" name="data-nascimento" required><br>

        <label for="rg">RG e Órgão Emissor:</label>
        <input type="text" id="rg" name="rg" required><br>

        <label for="data-emissao">Data de Emissão:</label>
        <input type="date" id="data-emissao" name="data-emissao" required><br>

        <label for="naturalidade">Naturalidade:</label>
        <input type="text" id="naturalidade" name="naturalidade"><br>

        <label for="nacionalidade">Nacionalidade:</label>
        <input type="text" id="nacionalidade" name="nacionalidade"><br>

        <label for="estado-civil">Estado Civil:</label>
        <input type="text" id="estado-civil" name="estado-civil"><br>

        <label for="conjuge">Cônjuge:</label>
        <input type="text" id="conjuge" name="conjuge"><br>

        <label for="rendimento-conjuge">Rendimento do Cônjuge:</label>
        <input type="text" id="rendimento-conjuge" name="rendimento-conjuge"><br>

        <label for="rendimento-titular">Rendimento do Titular:</label>
        <input type="text" id="rendimento-titular" name="rendimento-titular" required><br>

        <label for="atividade">Atividade Desenvolvida:</label>
        <input type="text" id="atividade" name="atividade" required><br>

        <label for="nome-mae">Nome da Mãe:</label>
        <input type="text" id="nome-mae" name="nome-mae" required><br>

        <label for="nome-pai">Nome do Pai:</label>
        <input type="text" id="nome-pai" name="nome-pai"><br><br>

        <button type="submit">Enviar</button>
    </form>

    <script>
        document.getElementById('cadastro-form').addEventListener('submit', function(e) {
            e.preventDefault();

            // Capturar os valores dos campos
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

            // Gerar PDF com jsPDF
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

            // Converte o PDF para Blob
            const pdfBlob = doc.output('blob');

            // Cria um link temporário para o PDF
            const pdfURL = URL.createObjectURL(pdfBlob);

            // Número do WhatsApp
            const whatsappNumber = '559870002002';

            // Monta a mensagem com o link do PDF
            const message = `Olá, segue o formulário preenchido: ${pdfURL}`;
            const whatsappLink = `https://wa.me/${whatsappNumber}?text=${encodeURIComponent(message)}`;

            // Abre o link do WhatsApp
            window.open(whatsappLink, '_blank');
        });
    </script>
</body>
</html>
