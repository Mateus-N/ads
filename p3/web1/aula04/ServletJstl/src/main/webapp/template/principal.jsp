<%@ page contentType="text/html;charset=UTF-8" language="java" isELIgnored="false"%>
<%@ taglib uri="http://java.sun.com/jstl/core" prefix="c" %>
<html>
<head>
    <title>Exemplo JSTL</title>
</head>
<body>
    <h1>Minha Lista</h1>
    <c:forEach var="valor" begin="1" end="10" step="1" >
        <ul>
            <li>${valor}</li>
        </ul>
    </c:forEach>
    <p>Atributo: ${nome}</p>
    <%@ include file="secundario.jsp" %>
</body>
</html>
