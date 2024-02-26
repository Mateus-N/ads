package br.edu.unifip;

import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import java.io.PrintWriter;

@WebServlet("/meuservlet")
public class MeuServlet extends HttpServlet {
    protected void doGet(HttpServletRequest request, HttpServletResponse response) {
        try {
            PrintWriter out = response.getWriter();
            out.println("<html>");
            out.println("<body>");
            out.println("<h1>Mateus</h1>");
            out.println("</body>");
            out.println("</html>");
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}
