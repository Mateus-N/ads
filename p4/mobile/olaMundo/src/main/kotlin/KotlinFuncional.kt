package org.example

fun main() {
    val languages = listOf("java", "C#", "JavaScript", "Kotlin")
    languages.forEach { println(it) }

    val numbers = listOf(4, 5, 6, 7, 8)
    numbers.forEach { number -> println(number) }

    println("Maior: ${numbers.maxBy { it }}")
    println("Somando 1: ${numbers.map { it + 1 }}")
    println("Pares: ${numbers.filter { it % 2 == 0 }}")

    val minhaFuncao: () -> Unit

    val livros = listOf(
        Livro(1, "O fim da Infância", "Aleph", 22.0),
        Livro(2, "Kotlin in Action", "Tech", 80.0),
        Livro(3, "Java: How to Program", "Tech", 120.0)
    )

    printLivros("Livros", livros)

    printLivros("Livros Tech", livros.filter { it.editora == "Tech" })

    printLivros("Livros caros", livros.filter { it.preco > 100 })
}

fun printLivros(titulo: String, livros: List<Livro>) {
    println("---$titulo---")
    livros.forEach { println(it) }
}

fun funcaoTeste(func: () -> Unit) : Unit {

}

data class Livro(
    val codigo: Int,
    val titulo: String,
    val editora: String,
    val preco: Double = 0.0
) {
    override fun toString(): String {
        return "#$codigo - $titulo ($editora) - R$$preco"
    }
}