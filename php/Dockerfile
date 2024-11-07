# imagem (instalador) desejado
FROM php:8.2-fpm

# rodar as instalações de dependências
RUN docker-php-ext-install pdo

# habilita o uso das dependências
RUN docker-php-ext-enable pdo

EXPOSE 8000

CMD ["php-fpm"]