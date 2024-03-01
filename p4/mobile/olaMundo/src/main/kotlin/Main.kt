package org.example

fun main() {
    val nome = "Mateus"
    val idade = 23
    val adulto = true
    val sobrenome = "Nunes"
    val peso = 56.5

    val nomeCompleto = "$nome $sobrenome"
    println(nomeCompleto)

    if (adulto) {
        println("é adulto")
    } else {
        println("não é adulto")
    }

    val linguagens = arrayOf("A", "B", "C")

    val linguagens2 = mutableListOf("A", "B", "C")
    linguagens2.add("D")
    println(linguagens2)

    for (i in linguagens2) {
        println(i)
    }

    val responsavel = if (adulto) {
        true
    } else {
        false
    }

    val status = "Concluido"
    when (status) {
        "Pendente" -> {

        }
        "Concluido" -> {

        }
        else -> {

        }
    }

    println("${somar(10, 10)}")
    mostrarSoma(10, 10)
    println("${subtrair(10, 10)}")

    val product = Product(1, "Mesa", 199.9)
    println(product)
}

fun somar(x: Int, y: Int): Int {
    return x + y
}

fun mostrarSoma(x: Int, y: Int): Unit {
    println(x + y)
}

fun subtrair(x: Int, y: Int) = x - y

data class Product(
    val id: Int,
    val description: String,
    val price: Double
)