<script>
  export let mode = 'logline';
  export let setMode;
</script>
<nav class="left-menu">
  <button on:click={() => setMode('logline')}>LogLine</button>
  <button on:click={() => setMode('communicator')}>Communicator</button>
  <button on:click={() => setMode('contracter')}>Contracter</button>
</nav>

<style>
  .left-menu { display: flex; flex-direction: column; gap: 0.5rem; width: 150px; }
  button { font-size: 1rem; }
</style>
