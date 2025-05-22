<script>
  export let fields = null;
</script>
<div class="right-menu">
  {#if fields}
    <pre>{JSON.stringify(fields, null, 2)}</pre>
  {/if}
</div>

<style>
  .right-menu { font-family: monospace; width: 200px; border-left: 1px solid #ccc; padding: 0.5rem; }
</style>
