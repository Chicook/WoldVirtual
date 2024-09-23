// BK_INICIO/seccion_1/angular/main.ts

import { Component } from '@angular/core';
import { platformBrowserDynamic } from '@angular/platform-browser-dynamic';
import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';

@Component({
  selector: 'app-root',
    template: `<h1>¡Bienvenido a tu web básica en Angular!</h1>`
    })
    class AppComponent {}

    @NgModule({
      declarations: [AppComponent],
        imports: [BrowserModule],
          bootstrap: [AppComponent]
          })
          class AppModule {}

          platformBrowserDynamic().bootstrapModule(AppModule);
          ##