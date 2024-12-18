import { defineStore } from 'pinia'
import speechesData from '@/assets/speeches_summary_buzzwords.json';

function calculateDuration(begin: string, end: string): string {
    const [beginHours, beginMinutes, beginSeconds] = begin.split(':').map(Number);
    const [endHours, endMinutes, endSeconds] = end.split(':').map(Number);

    const beginTimeInSeconds = beginHours * 3600 + beginMinutes * 60 + beginSeconds;
    const endTimeInSeconds = endHours * 3600 + endMinutes * 60 + endSeconds;

    const durationInSeconds = endTimeInSeconds - beginTimeInSeconds;
    const minutes = Math.floor(durationInSeconds / 60);
    const seconds = durationInSeconds % 60;

    return `${minutes.toString().padStart(2, '0')}:${seconds.toString().padStart(2, '0')}`;
}

function createHandle(name: string): string {
    return name
        .trim()
        .toLowerCase()
        .replace(/\s+/g, '_')
        .replace(/[^\w_]/g, '');
}

export const useSpeechesStore = defineStore('speeches', {
    state: () => ({
        speeches: [] as {
            name: string,
            speak_time: string,
            text: string,
            buzzwords: string[],
            summary: string,
            handle: string
        }[],
    }),
    actions: {
        loadSpeeches() {
            this.speeches = speechesData.map((speech: any) => ({
                name: speech.name,
                speak_time: calculateDuration(speech.beginSpeech, speech.endSpeech),
                buzzwords: speech.buzzwords,
                summary: speech.summary,
                text: speech.text,
                handle: createHandle(speech.name),
            }));
        },
    },
});
