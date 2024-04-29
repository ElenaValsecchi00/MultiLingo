<script setup>
import TheWelcome from '../components/TheWelcome.vue'
</script>
<script>
import { useI18n } from 'vue-i18n'
  export default {
    setup() {
      const { t } = useI18n()
      return { t }
    }
  }
</script>

<template>
  <main>
    <h1>{{ $t("home.header") }}</h1>
    <p>{{ $t("home.created_by") }}</p>
  </main>
</template>
