<script setup>
import { RouterLink, RouterView } from 'vue-router';

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
  <RouterView />
</template>

<style scoped>

@import url('https://fonts.googleapis.com/css2?family=Jua&display=swap');
html, body {
  font-family: 'Jua', sans-serif;
}

#app {
  font-family: 'Jua', sans-serif;
}


/*
@media (min-width: 1024px) {
  header {
    display: flex;
    place-items: center;
    padding-right: calc(var(--section-gap) / 2);
  }

  header .wrapper {
    display: flex;
    place-items: flex-start;
    flex-wrap: wrap;
  }

  nav {
    text-align: left;
    margin-left: -1rem;
    font-size: 1rem;

    padding: 1rem 0;
    margin-top: 1rem;
  }
}
*/
</style>
