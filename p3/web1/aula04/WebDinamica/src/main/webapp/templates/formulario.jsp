<%@ page contentType="text/html;charset=UTF-8" language="java" pageEncoding="UTF-8" isELIgnored="false" %>
<%@ page import="br.edu.unifip.Turma" %>
<!DOCTYPE html>
<html lang="pt-br">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <link rel="stylesheet" href="${pageContext.request.contextPath}/css/formulario.css">
  <title>Items</title>
</head>
<body>
  <div class="container">
    <h1 class="title">Novo aluno</h1>
    <form class="formulario" action="formulario" method="post">
      <label for="nome">Nome
        <input
          class="input"
          type="text"
          placeholder="Digite o nome"
          name="nome"
          required
        >
      </label>
      <label for="email">Email
        <input
          class="input"
          type="email"
          placeholder="Digite o email"
          name="email"
          required
        >
      </label>
      <label for="idade">Idade
        <input
          class="input"
          type="number"
          placeholder="Digite a idade"
          name="idade"
          required
        >
      </label>
      <label for="media">Média
        <input
          class="input"
          type="number"
          placeholder="Digite a média"
          name="media"
          required
        >
      </label>
      <input class="button" type="submit" value="Adicionar">
    </form>
  </div>
</body>
</html>