package br.edu.unifip;

import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import java.io.IOException;

@WebServlet("/formulario")
public class FormularioServlet extends HttpServlet {
    @Override
    protected void doGet(HttpServletRequest req, HttpServletResponse resp) throws ServletException, IOException {
        req.getRequestDispatcher("templates/formulario.jsp").forward(req, resp);
    }

    @Override
    protected void doPost(HttpServletRequest req, HttpServletResponse resp) throws ServletException, IOException {
        String nome = req.getParameter("nome");
        String email = req.getParameter("email");
        int idade = Integer.parseInt(req.getParameter("idade"));
        double media = Double.parseDouble(req.getParameter("media"));

        Turma.adicionarAluno(new Aluno(nome, email, idade, media));

        req.getRequestDispatcher("templates/items.jsp").forward(req, resp);
    }
}
