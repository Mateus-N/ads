package composicao;

import java.util.ArrayList;
import java.util.List;

public class Evento {
    private String nome;
    private String data;
    private String hora;
    private Organizador organizador;
    private Local local;
    private List<Participante> participantes = new ArrayList<Participante>();
    
    public String getNome() {
        return nome;
    }
    public void setNome(String nome) {
        this.nome = nome;
    }
    public String getData() {
        return data;
    }
    public void setData(String data) {
        this.data = data;
    }
    public String getHora() {
        return hora;
    }
    public void setHora(String hora) {
        this.hora = hora;
    }
    public Organizador getOrganizador() {
        return organizador;
    }
    public void setOrganizador(Organizador organizador) {
        this.organizador = organizador;
    }
    public Local getLocal() {
        return local;
    }
    public void setLocal(Local local) {
        this.local = local;
    }
    public List<Participante> getParticipantes() {
        return participantes;
    }

    public void adicionarParticipante(Participante participante) {
        participantes.add(participante);
    }

    public String verificaDisponibilidade(int quantidade) {
        boolean disponivel = local.verificarDisponibilidade(quantidade);

        if (disponivel) {
            return "O evento pode ser realizado no local";
        } else {
            return "O evento não pode ser realizado no local";
        }
    }

    public void imprimirListaDeParticipantes() {
        for (Participante participante : participantes) {
            System.out.println("Nome: " + participante.getNome());
            System.out.println("Email " + participante.getEmail());
        }
    }
}
