.open gefin.db;
CREATE TABLE IF NOT EXISTS clientes (
                    codigo INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
                    nome VARCHAR(100) NOT NULL,
                    pessoa CHAR(1),
                    cnpj_cpf VARCHAR(14) UNIQUE,
                    rg_ie VARCHAR(15),
                    telefone TEXT,
                    email TEXT,
                    endereco TEXT,
                    bairro TEXT,
                    cidade TEXT,
                    uf CHAR(2),
                    ativo INTEGER
                );