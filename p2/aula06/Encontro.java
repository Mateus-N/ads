package aula06;

public class Encontro {
    private int dia;
    private int mes;
    private String descricao;

    public int getDia() {
        return dia;
    }
    public void setDia(int dia) {
        if (mes == 0) {
            System.out.println("Adicione primeiramente um mês");
        } else if (ehDataValida(dia)) {
            this.dia = dia;
        } else {
            System.out.println("Dia inválido");
        }
    }
    public int getMes() {
        return mes;
    }
    public void setMes(int mes) {
        if (mes > 0 && mes <= 12) {
            this.mes = mes;
        }
    }
    public String getDescricao() {
        return descricao;
    }
    public void setDescricao(String descricao) {
        this.descricao = descricao;
    }

    private boolean ehDataValida(int dia) {
        if (ehFevereiroEValido(dia)) {
            return true;
        }
        if (ehMesComQuantidadeDeDiasValida(dia)) {
            return true;
        }
        return false;
    }

    private boolean ehFevereiroEValido(int dia) {
        if (mes == 2 && dia > 0 && dia <= 28) {
            return true;
        }
        return false;
    }

    private boolean ehMesComQuantidadeDeDiasValida(int dia) {
        if (mes <= 7 && mes % 2 == 1 || mes > 7 && mes % 2 == 0) {
            if (dia > 0 && dia <= 31) {
                return true;
            }
        } else {
            if (dia > 0 && dia <= 30) {
                return true;
            }
        }
        return false;
    }
}
