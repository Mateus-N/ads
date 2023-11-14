package br.edu.unifip;

import javax.servlet.RequestDispatcher;
import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import java.io.IOException;

@WebServlet("/encaminhamento")
public class EncaminhamentoServlet extends HttpServlet {
    @Override
    protected void doGet(HttpServletRequest req, HttpServletResponse resp) throws ServletException, IOException {
        String pagina = req.getParameter("pagina");
        RequestDispatcher dispatcher;

        if (pagina.equals("pagina1")) {
            dispatcher = req.getRequestDispatcher("templates/pagina1.jsp");
        } else if (pagina.equals("pagina2")) {
            dispatcher = req.getRequestDispatcher("templates/pagina2.jsp");
        } else {
            dispatcher = req.getRequestDispatcher("templates/erro.jsp");
        }

        dispatcher.forward(req, resp);
    }
}
