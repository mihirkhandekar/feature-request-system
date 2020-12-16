import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';

import { AppComponent } from './app.component';
import { SubmitFeedbackComponent } from './submit-feedback/submit-feedback.component';

import { ReactiveFormsModule } from '@angular/forms';
import { HttpClientModule } from '@angular/common/http';
import { ViewFeedbackComponent } from './view-feedback/view-feedback.component';


@NgModule({
  declarations: [
    AppComponent,
    SubmitFeedbackComponent,
    ViewFeedbackComponent
  ],
  imports: [
    BrowserModule,
    HttpClientModule,
    ReactiveFormsModule
  ],
  providers: [],
  bootstrap: [AppComponent]
})

export class AppModule { }
