<%@ page contentType="text/html;charset=UTF-8" language="java" pageEncoding="UTF-8" isELIgnored="false" %>
<%@ page import="br.edu.unifip.Aluno" %>
<%@ page import="br.edu.unifip.Turma" %>
<%@ page import="java.util.*" %>
<!DOCTYPE html>
<html lang="pt-br">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <link rel="stylesheet" href="${pageContext.request.contextPath}/css/styles.css">
  <title>Items</title>
</head>
<body>
  <div class="container">
    <h1>Alunos cadastrados</h1>
    <div class="alunos">
      <% 
        Turma turma = new Turma();
        List<Aluno> alunos = turma.getAlunos();
        for (Aluno aluno: alunos) { 
      %>
        <div class="card__aluno">
          <p><strong>Nome:</strong> <%= aluno.nome %></p>
          <p><strong>Email:</strong> <%= aluno.email %></p>
          <p><strong>Idade:</strong> <%= aluno.idade %></p>
          <p><strong>Media:</strong> <%= aluno.media %></p>
        </div>
      <% } %>
    </div>
  </div>
</body>
</html>