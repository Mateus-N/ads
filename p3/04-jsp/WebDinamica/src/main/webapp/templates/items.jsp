<%@ page contentType="text/html;charset=UTF-8" language="java" pageEncoding="UTF-8" isELIgnored="false" %>
<%@ page import="br.edu.unifip.Aluno" %>
<%@ page import="br.edu.unifip.Turma" %>
<%@ page import="java.util.*" %>
<!DOCTYPE html>
<html lang="pt-br">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <link rel="stylesheet" href="${pageContext.request.contextPath}/css/style.css">
  <title>Items</title>
</head>
<body>
  <div class="container">
    <header class="cabecalho">
      <h1 class="title">Alunos cadastrados</h1>
      <form action="formulario" method="get">
        <input type="submit" value="Adicionar novo aluno">
      </form>
    </header>
    <div class="alunos">
      <% 
        List<Aluno> alunos = Turma.getAlunos();
        for (Aluno aluno: alunos) { 
      %>
        <div class="card__aluno">
          <p><strong>Nome:</strong> <%= aluno.getNome() %></p>
          <p><strong>Email:</strong> <%= aluno.getEmail() %></p>
          <p><strong>Idade:</strong> <%= aluno.getIdade() %></p>
          <p><strong>Media:</strong> <%= aluno.getMedia() %></p>
        </div>
      <% } %>
    </div>
  </div>
</body>
</html>