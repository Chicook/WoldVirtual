// Program.cs
using Microsoft.AspNetCore.Hosting;
using Microsoft.Extensions.Hosting;

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
                                                                                                                                                                     