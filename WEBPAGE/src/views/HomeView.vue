<script setup lang="ts">
import { ref, computed } from 'vue';
import { useSpeechesStore } from '@/stores/speeches';
import warnung from "@/components/warnung.vue";

let isNavbarMenuActive = ref(false)
let searchTerm = ref("")
let searchQuery = ref('')
let maxResults = ref(5)
let showAllResults = ref(false)
let activeSearchFilter = {
  name: "Sprecher",
  active: true,
  placeholder: "Suche Sprecher...",
  search: "name"
}
let searchFilter = [
  {
    name: "Sprecher",
    active: true,
    placeholder: "Suche Sprecher...",
    search: "name"
  },
  {
    name: "Schlagworte",
    active: false,
    placeholder: "Suche Schlagwort...",
    search: "buzzword"
  },
  {
    name: "Textinhalt",
    active: false,
    placeholder: "Inhalt...",
    search: "text"
  }
]

const speechesStore = useSpeechesStore();
const speeches = computed(() => speechesStore.speeches);

</script>

<template>
  <!-- MAIN CONTENT -->
  <main class="flex flex-col space-y-10 max-w-2xl mx-auto p-4">
    <div class="text-xl  flex flex-col justify-center items-left h-full" id="title">
      <h2 class="text-4xl font-gruenetype font-bold">Reden des hessischen Landes-Parteitages der Grünen</h2>

      <warnung></warnung>


      <!-- REDEN -->

      <h3 class="mt-4">
        Die Reden des Landesparteitages:
      </h3>
      <ul class="grid lg:grid-cols-2 space-y-1">

        <li v-for="speech in speeches" class="bg-white rounded" :key="speech.name">
          <router-link :to="{
            name: 'Speeches',
            params: {
              speaker: speech.name.replace(/\s/g, '_').toLowerCase()
            },
          }" class="flex justify-between md:px-4 ">
            <p>
              {{ speech.name }}
            </p>
            <p>
              {{ speech.speak_time }}
            </p>
          </router-link>
        </li>

      </ul>

      <div class="flex flex-col bg-gruene-green rounded-lg p-4 mb-4 text-sm text-gruene-green-accent">
        <h3 class="">Quelle: Landesparteitag am 14. Dezember 2024</h3>
        <div>
          - 🔗 URL: https://www.youtube.com/live/L9ePHyT1fZM
        </div>
      </div>
    </div>

    <div id="how">
      <h3 class="text-xl font-bold">
        Vorgehen:
      </h3>
      <p>Die Reden wurden aus dem Livestream als Audiodatei herausgeschnitten.
        Anschließend mit dem Audio-zu-Text KI-Modell (<a class="text-blue-500" href="https://openai.com/blog/whisper/"
          target="_blank">OpenAI - Whisper</a>) zu Text umgewandelt.

        Unterbrechungen des Präsidiums sind teilweise im Fließtext enthalten.


      </p>
    </div>

  </main>
</template>
