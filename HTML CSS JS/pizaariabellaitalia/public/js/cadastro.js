window.addEventListener("load", () => {
    // Obter o formulário de cadastro pelo ID
    const mensagem = document.getElementById('mensagem');
    const formLogin = document.getElementById('formLogin');
    const formCadastro = document.getElementById('formCadastro');

    // Adicionar um ouvinte de evento para o evento 'submit' do formulário
    formLogin.addEventListener('submit', async function (event) {
        // Prevenir a ação padrão do formulário (envio)
        event.preventDefault();

        const formLogin = document.getElementById('formLogin');
        if (formLogin) {
            formLogin.addEventListener('submit', async function (event) {
                event.preventDefault();

                const email = document.getElementById('email').value;
                const password = document.getElementById('password').value;


                try {
                    // Fazer uma requisição POST para o endpoint '/api/register'
                    const response = await fetch('/api/login', {
                        method: 'POST',
                        headers: {
                            'Content-Type': 'application/json'
                        },
                        body: JSON.stringify({
                            email: email,
                            password: password
                        })
                    }
                    );

                    const result = await response.json();
                    // Verificar se a resposta da requisição foi bem-sucedida
                    if (response.ok) {
                        mensagem.textContent = 'Usuário logado com sucesso!';
                        mensagem.style.color = 'green';
                    } else {
                        // Obter a mensagem de erro da resposta e exibi-la
                        mensagem.textContent = result.error || "Erro ao efetuar login.";;
                        mensagem.style.color = 'red';
                    }
                } catch (error) {
                    // Exibir uma mensagem de erro em caso de falha na requisição
                    mensagem.textContent = 'Erro ao logar usuário. Verifique sua conexão.';
                    mensagem.style.color = 'red';
                }
            })
        }

        if (formCadastro) {
            formCadastro.addEventListener("submit", async function (event) {
                event.preventDefault();

                const username = document.getElementById("username").value;
                const email = document.getElementById("email").value;
                const password = document.getElementById("password").value;
                const confirmPassword = document.getElementById("password2").value;

                if (password !== confirmPassword) {
                    mensagem.textContent = "As senhas não coincidem!";
                    mensagem.style.color = "red";
                    return;
                }

                try {
                    const response = await fetch("/api/register", {
                        method: "POST",
                        headers: { "Content-Type": "application/json" },
                        body: JSON.stringify({ username, email, password }),
                    });

                    if (response.ok) {
                        mensagem.textContent = "Usuário registrado com sucesso!";
                        mensagem.style.color = "green";
                    } else {
                        const erro = await response.json();
                        mensagem.textContent = erro.error;
                        mensagem.style.color = "red";
                    }
                } catch (error) {
                    mensagem.textContent = "Erro ao registrar usuário.";
                    mensagem.style.color = "red";
                }
            });
        }
    });
});