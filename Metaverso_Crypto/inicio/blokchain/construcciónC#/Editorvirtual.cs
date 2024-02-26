// Program.cs
// Controllers/EditorController.cs
using Microsoft.AspNetCore.Hosting;
using Microsoft.Extensions.Hosting;
using System;
using Microsoft.AspNetCore.Mvc;

public class EditorController : Controller
{
    public IActionResult Index()
    {
        return View();
    }

    [HttpPost]
    public IActionResult GuardarEntorno([FromBody] string entorno)
    {
        // Lógica para guardar el entorno virtual, por ejemplo, almacenarlo en una base de datos.
        // Aquí, simplemente mostramos el entorno en la consola.
        Console.WriteLine("Entorno guardado:");
        Console.WriteLine(entorno);

        return Ok();
    }

    [HttpGet]
    public IActionResult CargarEntorno()
    {
        // Lógica para cargar el entorno virtual, por ejemplo, desde una base de datos.
        // Aquí, simplemente devolvemos un entorno de ejemplo.
        string entornoEjemplo = "{ \"elementos\": [ { \"tipo\": \"cubo\", \"posicion\": { \"x\": 0, \"y\": 0, \"z\": 0 } } ] }";
        
        return Ok(entornoEjemplo);
    }
}

class Program
{
    static void Main()
    {
        Console.WriteLine("¡Hola desde C#!");

        // Aquí puedes continuar agregando funcionalidades según tus necesidades.

        // Por ejemplo, puedes pedir al usuario que ingrese su nombre:
        Console.Write("Ingresa tu nombre: ");
        string nombre = Console.ReadLine();

        // Luego, puedes saludar al usuario por su nombre:
        Console.WriteLine($"Hola, {nombre}!");

        // Puedes seguir agregando más lógica y funcionalidades aquí.

        Console.WriteLine("Presiona cualquier tecla para salir.");
        Console.ReadKey();
    }
}

public class Program
{
    public static void Main(string[] args)
        {
                CreateHostBuilder(args).Build().Run();
                    }

                        public static IHostBuilder CreateHostBuilder(string[] args) =>
                                Host.CreateDefaultBuilder(args)
                                            .ConfigureWebHostDefaults(webBuilder =>
                                                        {
                                                                        webBuilder.UseStartup<Startup>();
                                                                                    });
                                                                                    }

                                                                                    // Startup.cs
                                                                                    using Microsoft.AspNetCore.Builder;
                                                                                    using Microsoft.AspNetCore.Hosting;
                                                                                    using Microsoft.Extensions.DependencyInjection;

                                                                                    public class Startup
                                                                                    {
                                                                                        public void ConfigureServices(IServiceCollection services)
                                                                                            {
                                                                                                    services.AddControllersWithViews();
                                                                                                        }

                                                                                                            public void Configure(IApplicationBuilder app, IWebHostEnvironment env)
                                                                                                                {
                                                                                                                        if (env.IsDevelopment())
                                                                                                                                {
                                                                                                                                            app.UseDeveloperExceptionPage();
                                                                                                                                                    }

                                                                                                                                                            app.UseRouting();

                                                                                                                                                                    app.UseEndpoints(endpoints =>
                                                                                                                                                                            {
                                                                                                                                                                                        endpoints.MapControllerRoute(
                                                                                                                                                                                                        name: "default",
                                                                                                                                                                                                                        pattern: "{controller=Home}/{action=Index}/{id?}");
                                                                                                                                                                                                                                });
                                                                                                                                                                                                                                    }
                                                                                                                                                                                                                                    }

                                                                                                                                                                                                                                    // Controllers/EditorController.cs
                                                                                                                                                                                                                                    using Microsoft.AspNetCore.Mvc;

                                                                                                                                                                                                                                    [ApiController]
                                                                                                                                                                                                                                    [Route("api/[controller]")]
                                                                                                                                                                                                                                    public class EditorController : ControllerBase
                                                                                                                                                                                                                                    {
                                                                                                                                                                                                                                        [HttpGet]
                                                                                                                                                                                                                                            public IActionResult Get()
                                                                                                                                                                                                                                                {
                                                                                                                                                                                                                                                        return Ok("¡Hola desde el servidor C# en ASP.NET Core!");
                                                                                                                                                                                                                                                            }
                                                                                                                                                                                         }
                                                                                                                                                                     
