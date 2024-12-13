<!DOCTYPE html>
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
            max-width: 800px;
            margin: auto;
            background: white;
            padding: 20px;
            border-radius: 8px;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
        }
        h1 {
            font-family: 'Dancing Script', cursive;
            text-align: center;
        }
        label {
            font-family: 'Dancing Script', cursive;
            font-size: 18px;
        }
        input, select {
            width: calc(100% - 20px);
            padding: 10px;
            margin: 10px 10px 20px 10px;
            border: 1px solid #ccc;
            border-radius: 4px;
            font-size: 16px;
            box-sizing: border-box;
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
        table {
            width: 100%;
            border-collapse: collapse;
            margin-bottom: 20px;
        }
        th, td {
            border: 1px solid #ddd;
            padding: 8px;
            text-align: left;
        }
        th {
            background-color: #f2f2f2;
        }
        .section-title {
            background-color: #d3eaf7;
            font-weight: bold;
            text-align: center;
            padding: 10px;
            margin-bottom: 10px;
        }
    </style>
    <link href="https://fonts.googleapis.com/css2?family=Dancing+Script:wght@400;600&display=swap" rel="stylesheet">
</head>
<body>
    <div class="form-container">
        <h1>Formulário de Cadastro</h1>
        <div class="section-title">DADOS DO CONSORCIADO</div>
        <form id="cadastro-form">
            <table>
                <tr>
                    <td>Nome do Cliente:</td>
                    <td><input type="text" id="nome" name="nome" required></td>
                </tr>
                <tr>
                    <td>Email do Cliente:</td>
                    <td><input type="email" id="email" name="email" required></td>
                </tr>
                <tr>
                    <td>Telefone(s) do Cliente:</td>
                    <td><input type="text" id="telefone" name="telefone" required></td>
                </tr>
                <tr>
                    <td>CPF:</td>
                    <td><input type="text" id="cpf" name="cpf" required></td>
                </tr>
                <tr>
                    <td>Data de Nascimento:</td>
                    <td><input type="date" id="nascimento" name="nascimento" required></td>
                </tr>
                <tr>
                    <td>RG e Órgão Emissor:</td>
                    <td><input type="text" id="rg" name="rg" required></td>
                </tr>
                <tr>
                    <td>Data de Emissão:</td>
                    <td><input type="date" id="emissao" name="emissao" required></td>
                </tr>
                <tr>
                    <td>Naturalidade:</td>
                    <td><input type="text" id="naturalidade" name="naturalidade" required></td>
                </tr>
                <tr>
                    <td>Nacionalidade:</td>
                    <td><input type="text" id="nacionalidade" name="nacionalidade" required></td>
                </tr>
            </table>

            <div class="section-title">DADOS DO PLANO</div>
            <label for="valor">Valor do Consórcio:</label>
            <input type="number" id="valor" name="valor" required>

            <label for="plano">Plano Escolhido:</label>
            <select id="plano" name="plano" required>
                <option value="">Selecione um plano</option>
                <option value="plano1">Plano 1</option>
                <option value="plano2">Plano 2</option>
                <option value="plano3">Plano 3</option>
            </select>

            <button type="submit" class="submit-button">Enviar</button>
        </form>
    </div>

    <script src="https://cdnjs.cloudflare.com/ajax/libs/jspdf/2.4.0/jspdf.umd.min.js"></script>
    <script>
        document.getElementById('cadastro-form').addEventListener('submit', function(e) {
            e.preventDefault();

            const nome = document.getElementById('nome').value;
            const cpf = document.getElementById('cpf').value;
            const valor = document.getElementById('valor').value;
            const plano = document.getElementById('plano').value;

            if (!nome || !cpf || !valor || !plano) {
                alert('Por favor, preencha todos os campos corretamente.');
                return;
            }

            // Gerar PDF com as informações preenchidas
            const { jsPDF } = window.jspdf;
            const doc = new jsPDF();

            doc.setFont('Helvetica', 'normal');
            doc.setFontSize(12);

            doc.text('Formulário de Cadastro', 105, 20, { align: 'center' });

            doc.text(`Nome Completo: ${nome}`, 20, 40);
            doc.text(`CPF: ${cpf}`, 20, 50);
            doc.text(`Valor do Consórcio: R$ ${valor}`, 20, 60);
            doc.text(`Plano Escolhido: ${plano}`, 20, 70);

            // Salvar PDF
            doc.save(`Formulario_${nome.replace(/\s+/g, '_')}.pdf`);

            alert('PDF gerado com sucesso!');
        });
    </script>
</body>
</html>
