package br.edu.unifip;

import java.util.ArrayList;
import java.util.List;

public class Turma {
    private List<Aluno> alunos = new ArrayList<>();

    public Turma() {
        alunos.add(new Aluno("Mateus", "mateus@email.com", 22, 8.5));
        alunos.add(new Aluno("Adrielly", "adrielly@email.com", 23, 8.9));
        alunos.add(new Aluno("Bruno", "bruno@email.com", 23, 9.5));
        alunos.add(new Aluno("Kelvin", "kevin@email.com", 23, 8.5));
    }

    public List<Aluno> getAlunos() {
        return alunos;
    }
}
