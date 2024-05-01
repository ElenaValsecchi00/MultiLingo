<script setup>
</script>

<template>
  <header>
    <p>{{ $t("home.header") }}</p>
    
  </header>
  <div id="flags">
    <RouterLink to="levels"><img src="https://cdn.countryflags.com/thumbs/italy/flag-square-250.png" alt="italian"></RouterLink>
    <button><img src="https://cdn.countryflags.com/thumbs/france/flag-square-250.png" alt="french"></button>
    <button><img src="https://cdn.countryflags.com/thumbs/united-kingdom/flag-square-250.png" alt="uk"></button>
    <button><img src="https://cdn.countryflags.com/thumbs/germany/flag-square-250.png" alt="germany"></button>
  </div>
  <p>{{ $t("home.choose_flag") }}</p>
  <RouterView />
</template>

<style scoped>

img{
  width: 100%;
}
#flags{
  display: grid;
  grid-auto-flow: row;
  grid-gap: 10px;
  row-gap: 20px;
  column-gap: 20px;
  grid-template-rows: auto auto;
  grid-template-columns: auto auto;
  justify-content: center;
  padding: 40px;
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
