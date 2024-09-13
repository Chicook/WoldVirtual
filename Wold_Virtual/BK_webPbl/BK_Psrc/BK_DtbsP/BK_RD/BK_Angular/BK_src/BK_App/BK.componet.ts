// angular/src/app/app.component.ts
import { Component, AfterViewInit } from '@angular/core';

@Component({
  selector: 'app-root',
    templateUrl: './app.component.html',
      styleUrls: ['./app.component.css']
      })
      export class AppComponent implements AfterViewInit {
        message = 'Esta es una aplicación Angular integrada con React y Python.';

          ngAfterViewInit() {
              // Cargar el componente React después de que la vista de Angular esté inicializada
                  import('../../../../react/src/index.jsx').then(module => {
                        module.renderReactComponent();
                            });
                              }
                              }
                              