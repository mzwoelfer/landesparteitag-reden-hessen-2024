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

    <warnung></warnung>

    <div id="article" v-if="currentSpeech">
      <div class="bg-white p-4 drop-shadow">
        <h2 class="text-2xl font-bold">Zusammenfassung:</h2>
        <p class="text-xl prose">{{ currentSpeech?.summary }}</p>
      </div>

      <div class="flex flex-col bg-gruene-tanne rounded-lg p-4 mb-4 text-sm text-gruene-green-accent" role="alert">
        <h2 class="text-2xl text-white prose font-bold">Schlagworte:</h2>
        <ul class="text-white text-xl list-inside">
          <li class="list-disc" v-for="word in currentSpeech.buzzwords" :key="word">{{ word }}</li>
        </ul>
      </div>

      <div class="bg-white p-4">
        <h2 class="text-2xl">REDE</h2>
        <p v-html="currentSpeech.text" class="text-xl prose"></p>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import { useRoute } from "vue-router"
import { computed } from 'vue';
import { useSpeechesStore } from '@/stores/speeches';
import warnung from "@/components/warnung.vue";


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