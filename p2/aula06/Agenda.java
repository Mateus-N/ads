package aula06;

import java.util.ArrayList;

public class Agenda {
    private ArrayList<Encontro> encontros;

    public Agenda() {
        encontros = new ArrayList<Encontro>();
    }

    public void imprimirEncontros() {
        for (int i = 0; i < encontros.size(); i++) {
            System.out.println(encontros.get(i).getDescricao());
        }
    }

    public void addEncontros(Encontro encontro) {
        encontros.add(encontro);
    }
}
