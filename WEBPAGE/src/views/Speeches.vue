<template>
  <div class="container max-w-2xl mx-auto p-2 space-y-4">
    <h1 class="text-3xl font-bold">{{ currentSpeech?.name }}</h1>
    <p>Redezeit: {{ currentSpeech?.speak_time }} </p>
    <div v-if="currentSpeech">
      <iframe class="w-full h-full h-64 md:h-96"
        :src="`https://www.youtube.com/embed/${youtube_id}?si=VtBwutTzcNjIDolM&amp;start=${startSeconds}`"
        title="YouTube video player" frameborder="0"
        allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share"
        allowfullscreen>
      </iframe>
    </div>
    <div class="flex bg-gruene-yellow rounded-lg p-4 mb-4 text-sm text-gruene-green-accent" role="alert">
      <svg class="w-5 h-5 inline mr-3 text-gruene-magenta" fill="currentColor" viewBox="0 0 20 20"
        xmlns="http://www.w3.org/2000/svg">
        <path fill-rule="evenodd"
          d="M18 10a8 8 0 11-16 0 8 8 0 0116 0zm-7-4a1 1 0 11-2 0 1 1 0 012 0zM9 9a1 1 0 000 2v3a1 1 0 001 1h1a1 1 0 100-2v-3a1 1 0 00-1-1H9z"
          clip-rule="evenodd"></path>
      </svg>

      <div class="text-xl">
        <h3>Warnung!</h3>
        Die Reden automatisiert von 💬 Audio-zu-Text 📜 erstellt.<br>
        Texte beinhalten Rechtschreib-, Grammatik- und Formatierungsfehler.
      </div>
    </div>

    <div id="article" v-if="currentSpeech">
      <div class="bg-white p-4 drop-shadow">
        <h2 class="text-xl font-bold">Zusammenfassung:</h2>
        <p class="text-2xl prose">{{ currentSpeech?.summary }}</p>
      </div>

      <div class="flex flex-col bg-gruene-green rounded-lg p-4 mb-4 text-sm text-gruene-green-accent" role="alert">
        <h2 class="text-xl prose font-bold text-gruene-yellow">Schlagworte:</h2>
        <ul class="text-white text-2xl list-inside">
          <li class="list-disc" v-for="word in currentSpeech.buzzwords" :key="word">{{ word }}</li>
        </ul>
      </div>

      <div class="bg-white p-4">
        <h2 class="text-2xl">REDE</h2>
        <p v-html="currentSpeech.text" class="text-2xl prose"></p>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import { useRoute } from "vue-router"
import { computed } from 'vue';
import { useSpeechesStore } from '@/stores/speeches';

const route = useRoute();
const store = useSpeechesStore();

const currentSpeech = computed(() =>
  store.speeches.find((speech) => speech.handle === route.params.speaker)
);

const youtubeId = computed(() =>
  currentSpeech.value?.youtube_id || 'L9ePHyT1fZM'
);

const startSeconds = computed(() => {
  const timeParts = currentSpeech.value?.speak_time.split(':').map(Number) || [0];
  return timeParts[0] * 60 + (timeParts[1] || 0);
});
</script>