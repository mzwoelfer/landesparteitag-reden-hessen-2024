import './style.css'

import { createApp } from 'vue'
import { createPinia } from 'pinia'

import App from './App.vue'
import router from './router'
import { useSpeechesStore } from './stores/speeches';

const app = createApp(App)

app.use(createPinia())
app.use(router)

const speechesStore = useSpeechesStore();
speechesStore.loadSpeeches();

app.mount('#app')
