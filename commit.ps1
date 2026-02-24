# commit.ps1
$mensagem = Read-Host "Mensagem do commit (Enter para padrão)"

if ([string]::IsNullOrWhiteSpace($mensagem)) {
    $mensagem = "Atualização: $(Get-Date -Format 'dd/MM/yyyy HH:mm')"
}

git add .
git commit -m "$mensagem"
git push

Write-Host "✅ Commit realizado com sucesso!" -ForegroundColor Green