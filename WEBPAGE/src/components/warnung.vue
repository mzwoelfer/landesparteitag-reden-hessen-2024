      <template>
        <div class="flex bg-gruene-tanne rounded-lg p-4 mb-4 text-sm text-white" role="alert">
          <svg class="w-5 h-5 inline mr-3 " fill="currentColor" viewBox="0 0 20 20" xmlns="http://www.w3.org/2000/svg">
            <path fill-rule="evenodd"
              d="M18 10a8 8 0 11-16 0 8 8 0 0116 0zm-7-4a1 1 0 11-2 0 1 1 0 012 0zM9 9a1 1 0 000 2v3a1 1 0 001 1h1a1 1 0 100-2v-3a1 1 0 00-1-1H9z"
              clip-rule="evenodd"></path>
          </svg>
          <div>
            <h3 class="text-xl">Warnung!</h3>
            <div class="flex flex-col">
              Die Reden wurden automatisiert von 💬 Audio-zu-Text 📜 erstellt.<br>
              Rechtschreib-, Grammatik- und Formatierungsfehler sind zu erwarten <br><br>

              Redezeiten: Begin der Rede bis Ende der Rede, inkl. Unterbrechungen durch das Präsidium <br>
              <p class="text-lg">
                Mehr dazu im <router-link class="underline" to="FAQ">FAQ</router-link>
              </p>
            </div>
          </div>
        </div>
      </template>
