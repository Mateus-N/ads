package br.edu.unifip;

import java.util.ArrayList;
import java.util.Collections;
import java.util.List;

public class Turma {
    private static List<Aluno> alunos = new ArrayList<>();

    static {
        Aluno[] alunosBase = {
                new Aluno("Mateus", "mateus@email.com", 22, 8.5),
                new Aluno("Adrielly", "adrielly@email.com", 23, 8.9),
                new Aluno("Bruno", "bruno@email.com", 23, 9.5),
                new Aluno("Kelvin", "kevin@email.com", 23, 8.5)
        };

        Collections.addAll(alunos, alunosBase);
    }

    public static List<Aluno> getAlunos() {
        return alunos;
    }

    public static void adicionarAluno(Aluno aluno) {
        alunos.add(aluno);
    }
}
