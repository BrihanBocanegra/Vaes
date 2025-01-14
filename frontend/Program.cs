var builder = WebApplication.CreateBuilder(args);

// Agregamos CORS para permitir peticiones desde el navegador al backend Python
builder.Services.AddCors();

var app = builder.Build();

// Configuramos CORS (en este ejemplo, permitimos todo para pruebas)
app.UseCors(policy => 
    policy.AllowAnyOrigin()
          .AllowAnyMethod()
          .AllowAnyHeader());

// Habilitamos la carpeta de archivos estáticos (wwwroot)
app.UseStaticFiles();

// Opción para servir un archivo "index.html" por defecto
app.MapFallbackToFile("index.html");

// Iniciamos la aplicación en el puerto 5000
app.Run();