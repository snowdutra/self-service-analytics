CREATE TABLE proprietarios (
    cpf VARCHAR(14) PRIMARY KEY,
    nome VARCHAR(100),
    cidade VARCHAR(100)
);

INSERT INTO proprietarios (cpf, nome, cidade) VALUES
('111.111.111-11', 'Carlos Silva', 'São Paulo'),
('222.222.222-22', 'Ana Souza', 'Rio de Janeiro'),
('333.333.333-33', 'Mariana Lima', 'Belo Horizonte'),
('444.444.444-44', 'João Pereira', 'Curitiba'),
('555.555.555-55', 'Fernanda Alves', 'Porto Alegre'),
('666.666.666-66', 'Ricardo Mendes', 'Salvador'),
('777.777.777-77', 'Juliana Rocha', 'Fortaleza'),
('888.888.888-88', 'Eduardo Martins', 'Recife'),
('999.999.999-99', 'Camila Barros', 'Brasília'),
('101.101.101-10', 'Lucas Nogueira', 'Manaus'),
('202.202.202-20', 'Patricia Gomes', 'Florianópolis'),
('303.303.303-30', 'André Carvalho', 'Vitória'),
('404.404.404-40', 'Bianca Ribeiro', 'Goiânia'),
('505.505.505-50', 'Thiago Costa', 'Natal'),
('606.606.606-60', 'Larissa Freitas', 'Belém');