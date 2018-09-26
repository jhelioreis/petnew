/*
VARIÁVEIS GLOBAIS
*/
var breadcrumb = [];
var selectedId = -1;
var categories = [];
var products = [];
var clients = [];
var providers = [];

/*
EVENTOS GLOBAIS
*/
$(function(){
	categories = localStorage.getItem("petshow_categories");
	categories = JSON.parse(categories);
	if(categories == null) {
		categories = [];
	}

	products = localStorage.getItem("petshow_products");
	products = JSON.parse(products);
	if(products == null) {
		products = [];
	}

	clients = localStorage.getItem("petshow_clients");
	clients = JSON.parse(clients);
	if(clients == null) {
		clients = [];
	}

	providers = localStorage.getItem("petshow_providers");
	providers = JSON.parse(providers);
	if(providers == null) {
		providers = [];
	}

	fillContent('Início','home');
});

/*
EVENTOS REFERENTES ÀS CATEGORIAS
*/
$(document).on("click", ".category-new", function() {
	selectedId = -1;
	fillContent('Nova Categoria', 'detailCategory', getCategory);
});

$(document).on("click", ".category-edit", function() {
	selectedId = parseInt($(this).attr("data-id"));
	fillContent(JSON.parse(categories[selectedId]).name, 'detailCategory', getCategory);
});

$(document).on("click", ".category-delete", function() {
	selectedId = parseInt($(this).attr("data-id"));
	if (!deleteCategory()) {
		alert("Erro ao salvar a categoria. Tente novamente.");
	} else {
		selectedId = -1;
		fillContent('Categorias', 'listCategories', getCategories);
	}
});

$(document).on("click", ".category-save", function() {
	if (!saveCategory()) {
		alert("Erro ao salvar a categoria. Tente novamente.");
	}
});

$(document).on("click", ".category-cancel", function() {
	selectedId = -1;
	fillContent('Categorias','listCategories', getCategories);
});

/*
FUNÇÕES REFERENTES ÀS CATEGORIAS
*/

//Salva uma categoria
function saveCategory() {
	try {
		if (selectedId == -1) {
			var category = JSON.stringify({
				code : $("#category-code").val(),
				name : $("#category-name").val()
			});
			categories.push(category);
		} else {
			categories[selectedId] = JSON.stringify({
				code : $("#category-code").val(),
				name : $("#category-name").val()
			});
		}
		localStorage.setItem("petshow_categories", JSON.stringify(categories));
		return true;
	} catch (error) {
		console.log(error);
		return false;
	}
}

//Remove uma categoria
function deleteCategory() {
	try {
		if(selectedId != -1)
		{
			categories.splice(selectedId, 1);
			selectedId = -1;
			return true;
		}
	} catch(error) {
		console.log(error);
		return false;
	}
}

//Lista as categorias cadastradas no sistema
function getCategories() {
	var rows = "";

	for (var i in categories) {
		var category = JSON.parse(categories[i]);
		rows += "<tr>";
		rows += "<td><i class=\"fa fa-pencil-square-o category-edit\" data-id=\"" + i + "\"></i><i class=\"fa fa-trash-o category-delete\" data-id=\"" + i + "\"></i></td>";
    rows += "<td class=\"right\">" + category.code + "</td>";
		rows += "<td>" + category.name + "</td>";
		rows += "</tr>";
	}

	$("#category-table").append(rows);
}

//
function getCategory() {
	//TODO: Resta setar o valor do campo na edição
	if (selectedId != -1) {
		var category = JSON.parse(categories[selectedId]);
		$("#category-code").val(category.code);
		$("#category-name").val(category.name);
	}
}

/*
EVENTOS REFERENTES AOS PRODUTOS
*/
$(document).on("click", ".product-new", function() {
	selectedId = -1;
	fillContent('Novo produto', 'detailProduct', getProduct);
});

$(document).on("click", ".product-edit", function() {
	selectedId = parseInt($(this).attr("data-id"));
	fillContent(JSON.parse(products[selectedId]).name, 'detailProduct', getProduct);
});

$(document).on("click", ".product-delete", function() {
	selectedId = parseInt($(this).attr("data-id"));
	if (!deleteProduct()) {
		alert("Erro ao salvar o produto. Tente novamente.");
	} else {
		selectedId = -1;
		fillContent('Produtos', 'listProducts', getProducts);
	}
});

$(document).on("click", ".product-save", function() {
	if (!saveProduct()) {
		alert("Erro ao salvar o produto. Tente novamente.");
	}
});

$(document).on("click", ".product-cancel", function() {
	selectedId = -1;
	fillContent('Produtos','listProducts', getProducts);
});

/*
FUNÇÕES REFERENTES AOS PRODUTOS
*/

//Salva um produto
function saveProduct() {
	try {
		if (selectedId == -1) {
			var product = JSON.stringify({
				code : $("#product-code").val(),
				name : $("#product-name").val(),
        category : $("#product-category").val()
			});
			products.push(product);
		} else {
			products[selectedId] = JSON.stringify({
				code : $("#product-code").val(),
				name : $("#product-name").val(),
        category : $("#product-category").val()
			});
		}
		localStorage.setItem("petshow_products", JSON.stringify(products));
		return true;
	} catch (error) {
		console.log(error);
		return false;
	}
}

//Remove um produto
function deleteProduct() {
	try {
		if(selectedId != -1)
		{
			products.splice(selectedId, 1);
			selectedId = -1;
			return true;
		}
	} catch(error) {
		console.log(error);
		return false;
	}
}

//Lista os produtos cadastrados no sistema
function getProducts() {
	var rows = "";

	for (var i in products) {
		var product = JSON.parse(products[i]);
		rows += "<tr>";
		rows += "<td><i class=\"fa fa-pencil-square-o product-edit\" data-id=\"" + i + "\"></i><i class=\"fa fa-trash-o product-delete\" data-id=\"" + i + "\"></i></td>";
    rows += "<td class=\"right\">" + product.code + "</td>";
		rows += "<td>" + product.name + "</td>";
    rows += "<td>" + product.category + "</td>";
		rows += "</tr>";
	}

	$("#product-table").append(rows);
}

//
function getProduct() {
	//TODO: Resta setar o valor do campo na edição
	if (selectedId != -1) {
		var product = JSON.parse(products[selectedId]);
		$("#product-code").val(product.code);
		$("#product-name").val(product.name);
    $("#product-category").val(product.category);
	}
}

/*
EVENTOS REFERENTES AOS CLIENTES
*/
$(document).on("click", ".client-new", function() {
	selectedId = -1;
	fillContent('Novo cliente', 'detailClient', getClient);
});

$(document).on("click", ".client-edit", function() {
	selectedId = parseInt($(this).attr("data-id"));
	fillContent(JSON.parse(clients[selectedId]).name, 'detailClient', getClient);
});

$(document).on("click", ".client-delete", function() {
	selectedId = parseInt($(this).attr("data-id"));
	if (!deleteClient()) {
		alert("Erro ao salvar o cliente. Tente novamente.");
	} else {
		selectedId = -1;
		fillContent('Clientes', 'listClients', getClients);
	}
});

$(document).on("click", ".client-save", function() {
	if (!saveClient()) {
		alert("Erro ao salvar o cliente. Tente novamente.");
	}
});

$(document).on("click", ".client-cancel", function() {
	selectedId = -1;
	fillContent('Clientes','listClients', getClients);
});

/*
FUNÇÕES REFERENTES AOS CLIENTES
*/

//Salva um cliente
function saveClient() {
	try {
		if (selectedId == -1) {
			var client = JSON.stringify({
				code : $("#client-code").val(),
				name : $("#client-name").val(),
        docno : $("#client-docno").val(),
        phone : $("#client-phone").val(),
        cellphone : $("#client-cellphone").val(),
        address : $("#client-address").val(),
        neighborhood : $("#client-neighborhood").val(),
        city : $("#client-city").val(),
        state : $("#client-state").val()
			});
			clients.push(client);
		} else {
			clients[selectedId] = JSON.stringify({
        code : $("#client-code").val(),
				name : $("#client-name").val(),
        docno : $("#client-docno").val(),
        phone : $("#client-phone").val(),
        cellphone : $("#client-cellphone").val(),
        address : $("#client-address").val(),
        neighborhood : $("#client-neighborhood").val(),
        city : $("#client-city").val(),
        state : $("#client-state").val()
			});
		}
		localStorage.setItem("petshow_clients", JSON.stringify(clients));
		return true;
	} catch (error) {
		console.log(error);
		return false;
	}
}

//Remove um cliente
function deleteClient() {
	try {
		if(selectedId != -1)
		{
			clients.splice(selectedId, 1);
			selectedId = -1;
			return true;
		}
	} catch(error) {
		console.log(error);
		return false;
	}
}

//Lista os clientes cadastrados no sistema
function getClients() {
	var rows = "";

	for (var i in clients) {
		var client = JSON.parse(clients[i]);
		rows += "<tr>";
		rows += "<td><i class=\"fa fa-pencil-square-o client-edit\" data-id=\"" + i + "\"></i><i class=\"fa fa-trash-o client-delete\" data-id=\"" + i + "\"></i></td>";
    rows += "<td class=\"right\">" + client.code + "</td>";
		rows += "<td>" + client.docno + "</td>";
    rows += "<td>" + client.name + "</td>";
		rows += "</tr>";
	}

	$("#client-table").append(rows);
}

//
function getClient() {
	//TODO: Resta setar o valor do campo na edição
	if (selectedId != -1) {
		var client = JSON.parse(clients[selectedId]);
		$("#client-code").val(client.code);
		$("#client-name").val(client.name);
    $("#client-docno").val(client.docno);
    $("#client-phone").val(client.phone);
    $("#client-cellphone").val(client.cellphone);
    $("#client-address").val(client.address);
    $("#client-neighborhood").val(client.neighborhood);
    $("#client-city").val(client.city);
    $("#client-state").val(client.state);
	}
}

/*
EVENTOS REFERENTES AOS FORNECEDORES
*/
$(document).on("click", ".provider-new", function() {
	selectedId = -1;
	fillContent('Novo fornecedor', 'detailProvider', getProvider);
});

$(document).on("click", ".provider-edit", function() {
	selectedId = parseInt($(this).attr("data-id"));
	fillContent(JSON.parse(providers[selectedId]).name, 'detailProvider', getProvider);
});

$(document).on("click", ".provider-delete", function() {
	selectedId = parseInt($(this).attr("data-id"));
	if (!deleteProvider()) {
		alert("Erro ao salvar o fornecedor. Tente novamente.");
	} else {
		selectedId = -1;
		fillContent('Fornecedors', 'listProviders', getProviders);
	}
});

$(document).on("click", ".provider-save", function() {
	if (!saveProvider()) {
		alert("Erro ao salvar o fornecedor. Tente novamente.");
	}
});

$(document).on("click", ".provider-cancel", function() {
	selectedId = -1;
	fillContent('Fornecedors','listProviders', getProviders);
});

/*
FUNÇÕES REFERENTES AOS FORNECEDORES
*/

//Salva um fornecedor
function saveProvider() {
	try {
		if (selectedId == -1) {
			var provider = JSON.stringify({
				code : $("#provider-code").val(),
				name : $("#provider-name").val(),
        docno : $("#provider-docno").val(),
        phone : $("#provider-phone").val(),
        cellphone : $("#provider-cellphone").val(),
        address : $("#provider-address").val(),
        neighborhood : $("#provider-neighborhood").val(),
        city : $("#provider-city").val(),
        state : $("#provider-state").val()
			});
			providers.push(provider);
		} else {
			providers[selectedId] = JSON.stringify({
        code : $("#provider-code").val(),
				name : $("#provider-name").val(),
        docno : $("#provider-docno").val(),
        phone : $("#provider-phone").val(),
        cellphone : $("#provider-cellphone").val(),
        address : $("#provider-address").val(),
        neighborhood : $("#provider-neighborhood").val(),
        city : $("#provider-city").val(),
        state : $("#provider-state").val()
			});
		}
		localStorage.setItem("petshow_providers", JSON.stringify(providers));
		return true;
	} catch (error) {
		console.log(error);
		return false;
	}
}

//Remove um fornecedor
function deleteProvider() {
	try {
		if(selectedId != -1)
		{
			providers.splice(selectedId, 1);
			selectedId = -1;
			return true;
		}
	} catch(error) {
		console.log(error);
		return false;
	}
}

//Lista os fornecedores cadastrados no sistema
function getProviders() {
	var rows = "";

	for (var i in providers) {
		var provider = JSON.parse(providers[i]);
		rows += "<tr>";
		rows += "<td><i class=\"fa fa-pencil-square-o provider-edit\" data-id=\"" + i + "\"></i><i class=\"fa fa-trash-o provider-delete\" data-id=\"" + i + "\"></i></td>";
    rows += "<td class=\"right\">" + provider.code + "</td>";
		rows += "<td>" + provider.docno + "</td>";
    rows += "<td>" + provider.name + "</td>";
		rows += "</tr>";
	}

	$("#provider-table").append(rows);
}

//
function getProvider() {
	//TODO: Resta setar o valor do campo na edição
	if (selectedId != -1) {
		var provider = JSON.parse(providers[selectedId]);
		$("#provider-code").val(provider.code);
		$("#provider-name").val(provider.name);
    $("#provider-docno").val(provider.docno);
    $("#provider-phone").val(provider.phone);
    $("#provider-cellphone").val(provider.cellphone);
    $("#provider-address").val(provider.address);
    $("#provider-neighborhood").val(provider.neighborhood);
    $("#provider-city").val(provider.city);
    $("#provider-state").val(provider.state);
	}
}

/*
FUNÇÕES AUXILIARES
*/
//Carrega parte de uma tela na área de conteúdo.
function fillContent(name, link, callback) {
  breadcrumb.push([name, link]);
  $("#content").load("html/" + link + ".html", "", updateBreadcrumb);
	if (callback != null) {
		callback();
	}
}

//Atualiza o breadcrumb nas telas.
function updateBreadcrumb() {
    var content = "";
    for (var i = Math.min(5, breadcrumb.length) - 1; i >= 0 ; i--) {
      var item = breadcrumb[breadcrumb.length - i - 1];
      content += " <i class='fa fa-angle-right'></i> <a href=\"\" onClick=\"javascript:fillContent('" + item[0] +  "','" + item[1] + "');\">" + item[0] + "</a>";
    }

    $('#breadcrumb').html(content);
}
