<script>
  import LeftMenu from '$lib/LeftMenu.svelte';
  import RightMenu from '$lib/RightMenu.svelte';
</script>

<div class="layout">
  <aside class="left"><LeftMenu /></aside>
  <main class="center"><slot /></main>
  <aside class="right"><RightMenu /></aside>
</div>

<style>
.layout { display: grid; grid-template-columns: 200px 1fr 200px; height: 100vh; }
.left, .right { background: #f4f4f4; padding: 0.5rem; overflow-y: auto; }
.center { padding: 1rem; overflow-y: auto; }
@media (max-width: 600px) {
  .layout { grid-template-columns: 1fr; grid-template-rows: auto 1fr auto; }
  .left, .right { display: none; }
}
</style>
