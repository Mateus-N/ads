package org.example

fun main() {
    val produtos = listOf(
        Produto(1, "PS5", 3999.0, 4, "Games"),
        Produto(2, "XBOX Series X", 4350.0, 6, "Games"),
        Produto(3, "Notebook", 2999.0, 0, "Hardware"),
        Produto(4, "Sherlock Holmes", 49.9, 8, "Livros"),
        Produto(5, "Alice no país das maravilhas", 39.9, 12, "Livros"),
        Produto(6, "Os três mosqueteiros", 44.9, 4, "Livros")
    )

    imprimirProdutos("Produtos", produtos)
    imprimirProdutos("Produtos - Games", produtos.filter { it.categoria == "Games" })
    imprimirProdutos("Produtos - Preço menos que 2000", produtos.filter { it.preco < 2000 })
    imprimirProdutos("Produtos - Sem Estoque", produtos.filter { it.estoque == 0 })
    imprimirProdutos("Produtos - Livros", produtos.filter { it.categoria == "Livros" && it.estoque < 10 })
}

fun imprimirProdutos(titulo: String, produtos: List<Produto>) : Unit {
    println("---$titulo---")
    produtos.forEach { println(it) }
}

data class Produto(
    val codigo: Int,
    val nome: String,
    val preco: Double,
    val estoque: Int,
    val categoria: String
) {
    override fun toString(): String {
        return "#$codigo - $nome"
    }
}