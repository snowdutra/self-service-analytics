db = db.getSiblingDB('imobiliaria');

db.imoveis.insertMany([
  { endereco: "Rua A, 123", cidade: "São Paulo", valor: 750000, metragem: 120, cpf_proprietario: "111.111.111-11" },
  { endereco: "Rua B, 456", cidade: "Rio de Janeiro", valor: 680000, metragem: 95, cpf_proprietario: "222.222.222-22" },
  { endereco: "Rua C, 789", cidade: "Belo Horizonte", valor: 820000, metragem: 140, cpf_proprietario: "333.333.333-33" },
  { endereco: "Rua D, 111", cidade: "Curitiba", valor: 590000, metragem: 88, cpf_proprietario: "444.444.444-44" },
  { endereco: "Rua E, 222", cidade: "Porto Alegre", valor: 610000, metragem: 92, cpf_proprietario: "555.555.555-55" },
  { endereco: "Rua F, 333", cidade: "Salvador", valor: 730000, metragem: 110, cpf_proprietario: "666.666.666-66" },
  { endereco: "Rua G, 444", cidade: "Fortaleza", valor: 540000, metragem: 85, cpf_proprietario: "777.777.777-77" },
  { endereco: "Rua H, 555", cidade: "Recife", valor: 690000, metragem: 100, cpf_proprietario: "888.888.888-88" },
  { endereco: "Rua I, 666", cidade: "Brasília", valor: 880000, metragem: 150, cpf_proprietario: "999.999.999-99" },
  { endereco: "Rua J, 777", cidade: "Manaus", valor: 470000, metragem: 75, cpf_proprietario: "101.101.101-10" },
  { endereco: "Rua P, 404", cidade: "São Paulo", valor: 780000, metragem: 130, cpf_proprietario: "111.111.111-11" },
  { endereco: "Rua Q, 505", cidade: "Rio de Janeiro", valor: 710000, metragem: 105, cpf_proprietario: "222.222.222-22" }
]);