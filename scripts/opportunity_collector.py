logging.info("Starting collection for sources=%s since=%s", sources, args.since)
    counts = run_collect(
        sources=sources,
        since=args.since,
        persist=not args.no_persist,
        export=args.export,
    )
    logging.info("Completed collection: %s", counts)


if __name__ == "__main__":
    main()
