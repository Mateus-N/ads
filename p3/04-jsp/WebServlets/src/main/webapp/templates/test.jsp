<%@ page contentType="text/html;charset=UTF-8" language="java" pageEncoding="UTF-8" isELIgnored="false" %>
<html>
<head>
    <title>Exemplo de JSP</title>
</head>
<body>

    <h1>Olá, mundo!</h1>
    <p>Aqui está um exemplo de página JSP.</p>
    <p>Valor da variável: ${nome}</p>

    <form action="hello" method="post">
        <input type="submit" value="Ir para outra página">
    </form>

</body>
</html>