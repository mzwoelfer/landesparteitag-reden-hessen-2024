<template>
  <div class="flex flex-col h-full bg-gruene-sand">
    <nav class="flex items-center justify-between flex-wrap bg-gruene-tanne p-6">
      <div class="flex items-center text-white mr-6">
        <router-link class="flex items-center font-bold space-x-2" to="/">
          <img class="w-10 h-10"
            src="https://stadt.gruene-giessen.de/wp-content/themes/sunflower/assets/img/sunflower.svg" alt="">
          <h1 class="text-white text-3xl tracking-tight">GRÜNE Hessen Landesparteitags Reden 2024</h1>
        </router-link>
      </div>
    </nav>

    <router-view class="h-full" :key="$route.fullPath" />

    <!-- FOOTER -->
    <footer class="bg-gruene-tanne">
      <div class="py-2 px-3">
        <div class="space-x-4 ">
          <router-link class="text-white" to="/faq">
            FAQ
          </router-link>
        </div>

        <a href="https://github.com/mzwoelfer/" target="_blank"
          class="h-10 flex text-white justify-center items-center space-x-4">
          <p class="">
            Martin Fabian Zwölfer
          </p>

          <svg class="text-white w-6 h-6 fill-current" viewBox="0 0 98 96" xmlns="http://www.w3.org/2000/svg">
            <path fill-rule="evenodd" clip-rule="evenodd"
              d="M48.854 0C21.839 0 0 22 0 49.217c0 21.756 13.993 40.172 33.405 46.69 2.427.49 3.316-1.059 3.316-2.362 0-1.141-.08-5.052-.08-9.127-13.59 2.934-16.42-5.867-16.42-5.867-2.184-5.704-5.42-7.17-5.42-7.17-4.448-3.015.324-3.015.324-3.015 4.934.326 7.523 5.052 7.523 5.052 4.367 7.496 11.404 5.378 14.235 4.074.404-3.178 1.699-5.378 3.074-6.6-10.839-1.141-22.243-5.378-22.243-24.283 0-5.378 1.94-9.778 5.014-13.2-.485-1.222-2.184-6.275.486-13.038 0 0 4.125-1.304 13.426 5.052a46.97 46.97 0 0 1 12.214-1.63c4.125 0 8.33.571 12.213 1.63 9.302-6.356 13.427-5.052 13.427-5.052 2.67 6.763.97 11.816.485 13.038 3.155 3.422 5.015 7.822 5.015 13.2 0 18.905-11.404 23.06-22.324 24.283 1.78 1.548 3.316 4.481 3.316 9.126 0 6.6-.08 11.897-.08 13.526 0 1.304.89 2.853 3.316 2.364 19.412-6.52 33.405-24.935 33.405-46.691C97.707 22 75.788 0 48.854 0z" />
          </svg>
        </a>
      </div>
    </footer>

  </div>
</template>

<script setup lang="ts">
import { useRouter } from 'vue-router'

const router = useRouter()



</script>